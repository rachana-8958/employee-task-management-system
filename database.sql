'''---------database--------'''
CREATE DATABASE etms;
USE etms;
CREATE TABLE users (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'employee') NOT NULL
);
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    full_name VARCHAR(150),
    email VARCHAR(150),
    FOREIGN KEY (userid) REFERENCES users(userid) ON DELETE CASCADE
);
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(200),
    description TEXT,
    start_date DATE,
    end_date DATE
);
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT,
    task_name VARCHAR(200),
    description TEXT,
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    deadline DATE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
CREATE TABLE employee_tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    task_id INT,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    progress INT DEFAULT 0,
    status ENUM('assigned', 'in_progress', 'completed') DEFAULT 'assigned',
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE
);
