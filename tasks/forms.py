# from django import forms
# from .models import Task
# from django.utils import timezone

# class TaskForm(forms.ModelForm):
#     due_date = forms.DateTimeField(
#         required=False,
#         widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#         label='Due Date'
#     )

#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'status', 'priority', 'due_date', 'notify']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-select'}),
#             'priority': forms.Select(attrs={'class': 'form-select'}),
#             'notify': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }
#         labels = {
#             'title': 'Title',
#             'description': 'Description',
#             'status': 'Status',
#             'priority': 'Priority',
#             'notify': 'Enable Notification',
#         }

#     def clean_due_date(self):
#         data = self.cleaned_data.get('due_date')
#         if data and data < timezone.now():
#             raise forms.ValidationError('Due date must be in the future.')
#         return data
