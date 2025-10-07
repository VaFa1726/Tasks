🌟 Project Overview
Daily Dose is a sleek, priority-based task management system built with Django. It helps you organize your day by allowing you to add, categorize, and prioritize your tasks with simple yet powerful controls. Forget missing deadlines—our built-in notification feature ensures you’re always ahead of your schedule!

✨ Key Features
This application is designed to be your ultimate daily organizer, featuring:

🎯 Flexible Task Management
➕ Create, Edit, and Delete: Easily add new tasks, update their details, or permanently remove them.

📝 Detailed Fields: Each task includes a Title, Description, Due Date, and optional Notification flag.

🚦 Status and Priority Levels
✅ Dynamic Status Tracking: Toggle tasks between three clear states:

TODO ➡️ (Not started)

DOING ➡️ (In progress)

DONE ➡️ (Completed)

🔥 Priority Setting: Assign importance to tasks using a simple scale for better focus:

LOW

MEDIUM

HIGH

🔔 Smart Notifications & Filtering
⏰ 24-Hour Notifications: Get a notification for tasks whose due_date is less than 24 hours away (as implemented in is_due_soon()).

🔎 Powerful Filtering: View your tasks based on Status (e.g., only "Doing" tasks) or Priority (e.g., only "High" priority tasks).

🔄 Smart Ordering: Sort your task list by due_date or by priority to tackle the most important work first.

⚙️ Technical Stack
Backend Framework: Django (Python)

Database: Default SQLite (or easily configurable to PostgreSQL/MySQL)

Frontend: HTML/CSS (Utilizing Django Forms)
