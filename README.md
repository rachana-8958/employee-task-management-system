EMPLOYEE TASK MANAGEMENT SYSTEM 


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


<img width="500" height="500" alt="Screenshot 2026-04-05 212647" src="https://github.com/user-attachments/assets/b53a1403-acaf-4e79-91a7-e62bb4e8e098" />



User logs in (Admin / Employee)

System checks credentials and role


👨‍💼 Step 2: Admin Actions



<img width="509" height="500" alt="Screenshot 2026-04-05 212414" src="https://github.com/user-attachments/assets/e6eaf047-44ec-4a8a-9d35-07c51d113591" />



Admin adds new tasks




<img width="494" height="500" alt="Screenshot 2026-04-05 212618" src="https://github.com/user-attachments/assets/92b4bf70-152e-4e5b-87be-3b0d598dfca0" />



Assigns tasks to employees



<img width="503" height="500" alt="Screenshot 2026-04-05 212636 - Copy" src="https://github.com/user-attachments/assets/aad5fdcd-ca96-496a-8c3f-b2ed627e7e64" />



Tracks progress in dashboard




<img width="519" height="500" alt="Screenshot 2026-04-05 212414" src="https://github.com/user-attachments/assets/edf7e8b0-b0af-4ce8-af53-46c29ff16163" />





👨‍💻 Step 3: Employee Actions


Employee logs in

Views assigned tasks

Updates task status


<img width="509" height="505" alt="image" src="https://github.com/user-attachments/assets/d41e5540-7d61-4e37-a185-2cd19fbac861" />


can view task list



<img width="508" height="507" alt="image" src="https://github.com/user-attachments/assets/b81213cc-8902-44ba-afd0-799530683d2d" />


employee can change password and their personal details by clicking on profile option



<img width="509" height="500" alt="image" src="https://github.com/user-attachments/assets/cada68ce-51a1-42f4-8f9a-84d0632eeb31" />



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
