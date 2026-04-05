1. Project Overview

The Employee Task Management System (ETMS) is a web-based application developed to streamline task allocation and monitoring within an organization. It allows administrators to assign tasks to employees, track their progress, and manage deadlines efficiently, while employees can view, update, and complete their assigned tasks.

This system improves productivity, accountability, and communication between administrators and employees.


🎯 2. Objective of the Project

To automate task assignment and tracking
To reduce manual work and improve efficiency
To monitor employee performance
To ensure timely task completion using deadlines
To provide a centralized system for task management

🏗️ 3. System Architecture


The project follows a client-server architecture:

Frontend (Client Side):

HTML, CSS, JavaScript

Displays UI (dashboard, forms, tables)

Backend (Server Side):

Python with Flask

Handles logic, routing, and database operations

Database:

SQLite / MySQL

Stores users, employees, tasks, and assignments

🧠 4. Modules in the System

👨‍💼 Admin Module


Admin has full control over the system:


Login securely

Add tasks

Assign tasks to employees

View all employees

Track task progress

Monitor completed/pending tasks

Delete tasks or assignments

👨‍💻 Employee Module

Employee interacts with assigned tasks:


Login securely

View assigned tasks

Update task status:

Pending

In Progress

Completed

Track progress percentage

View deadlines

Manage profile (edit details, change password)


🗄️ 5. Database Design


Tables Used:

🧾 Users Table

userid (Primary Key)

username

password

role (admin/employee)

👥 Employees Table

emp_id (Primary Key)

userid (Foreign Key)

full_name

email


📋 Tasks Table

task_id (Primary Key)

task_name

description

deadline


🔗 Employee_Tasks Table

id (Primary Key)

emp_id (Foreign Key)

task_id (Foreign Key)

status
progress


⚙️ 6. Working Flow of the System

🔐 Step 1: Login

User logs in (Admin / Employee)

System checks credentials and role

👨‍💼 Step 2: Admin Actions

Admin adds new tasks

Assigns tasks to employees

Tracks progress in dashboard

👨‍💻 Step 3: Employee Actions

Employee logs in

Views assigned tasks

Updates task status

🔄 Step 4: Real-time Update

Status updated by employee

Reflected instantly in admin dashboard


🔥 7. Key Features

Role-based authentication 🔐

Task assignment and tracking 📋

Progress percentage display 📊

Deadline management ⏰

Late task detection 🔴

Responsive UI 📱

Profile management 👤

Dashboard analytics 📈

🔴 8. Special Feature – Late Task Detection

System compares:

Task deadline

Current date

If deadline passed & not completed:

👉 Marked as Late (Red Highlight)

📊 9. Dashboard Features

Admin Dashboard:

Total tasks

Total employees

Task status counts

Assigned task list

Employee Dashboard:

Total tasks

Pending tasks

Completed tasks

Task cards with progress


🧩 10. Technologies Used

Backend: Python (Flask)

Frontend: HTML, CSS, JavaScript

Database: SQLite / MySQL

Deployment: PythonAnywhere


⚠️ 11. Challenges Faced

Database migration (MySQL → SQLite)

Deployment issues on PythonAnywhere

Handling date comparison errors

Managing role-based authentication

UI responsiveness for mobile


🧠 12. Learnings from the Project

Full-stack web development using Flask

Database design and relationships

Session management and authentication

Debugging real-world errors

Deployment and hosting


🔮 13. Future Enhancements

Email notifications 📩

File upload for tasks 📁

Real-time updates (AJAX)

Project-based task grouping 📌

Mobile app integration 📱


🎯 14. Conclusion


The ETMS project successfully demonstrates how task management can be automated using web technologies. It enhances productivity, ensures accountability, and provides an efficient way to monitor employee performance in real-time.
