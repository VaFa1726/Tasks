from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.utils import timezone
from django.forms import modelform_factory
from .models import Task
from django import forms


TaskForm = modelform_factory(
    Task,
    fields=['title','description','status','priority','due_date','notify'],
    widgets={
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'status': forms.Select(attrs={'class':'form-select'}),
        'priority': forms.Select(attrs={'class':'form-select'}),
        'due_date': forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}),
        'notify': forms.CheckboxInput(attrs={'class':'form-check-input'})
    }
)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        order = self.request.GET.get('order') 

        if status in ['todo', 'doing', 'done']:
            qs = qs.filter(status=status)
        if priority in ['low', 'medium', 'high']:
            qs = qs.filter(priority=priority)

        if order == 'due':
            qs = qs.order_by('due_date')
        elif order == 'priority':
            qs = qs.order_by('priority', 'due_date')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        due_soon = Task.objects.filter(notify=True).filter(due_date__isnull=False)
        due_soon = [t for t in due_soon if t.is_due_soon()]
        context['due_soon'] = due_soon
        context['filter_status'] = self.request.GET.get('status', '')
        context['filter_priority'] = self.request.GET.get('priority', '')
        context['order'] = self.request.GET.get('order', '')
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm  
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        messages.success(self.request, 'Task added successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please fill out the form correctly.')
        return super().form_invalid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm   
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please fill out the form correctly.')
        return super().form_invalid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Task deleted successfully.')
        return super().delete(request, *args, **kwargs)


class ToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.status != 'done':
            task.status = 'done'
            messages.success(request, f'"{task.title}" marked as completed.')
        else:
            task.status = 'todo'
            messages.success(request, f'"{task.title}" marked as not completed.')
        task.save()
        return redirect('tasks:list')
