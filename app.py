from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
from datetime import date,datetime

app = Flask(__name__)
app.secret_key = "secret"

# ✅ DATABASE CONNECTION (AUTO PATH)
def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "etms.db")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# ✅ AUTO CREATE TABLES
def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER,
        full_name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT,
        description TEXT,
        deadline DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        task_id INTEGER,
        status TEXT DEFAULT 'pending',
        progress INTEGER DEFAULT 0
    )
    """)

    # ✅ AUTO ADMIN
    cursor.execute("SELECT * FROM users WHERE role='admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users(username,password,role) VALUES(?,?,?)",
            ("admin", "admin123", "admin")
        )

    db.commit()


# ✅ RUN INIT
with app.app_context():
    init_db()


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("home.html")


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users(username,password,role) VALUES(?,?,?)",
            (request.form['username'], request.form['password'], 'employee')
        )

        userid = cursor.lastrowid

        cursor.execute(
            "INSERT INTO employees(userid,full_name,email) VALUES(?,?,?)",
            (userid, request.form['full_name'], request.form['email'])
        )

        db.commit()
        return redirect('/login')

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "SELECT userid, role FROM users WHERE username=? AND password=?",
            (request.form['username'], request.form['password'])
        )

        user = cursor.fetchone()

        if user:
            session['userid'] = user['userid']
            session['role'] = user['role']
            return redirect('/admin' if user['role']=='admin' else '/employee')

        return "Invalid Login"

    return render_template("login.html")


# ---------------- ADMIN DASHBOARD ----------------
@app.route('/admin')
def admin():
    if session.get('role') != 'admin':
        return "Unauthorized"

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM employee_tasks WHERE status='pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM employee_tasks WHERE status='in_progress'")
    in_progress = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM employee_tasks WHERE status='completed'")
    completed = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks")
    task_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM employees")
    employee_count = cursor.fetchone()[0]

    cursor.execute("SELECT emp_id, full_name, email FROM employees")
    employees = cursor.fetchall()

    cursor.execute("""
    SELECT 
        employees.full_name,
        tasks.task_name,
        employee_tasks.status
    FROM employee_tasks
    JOIN employees ON employee_tasks.emp_id = employees.emp_id
    JOIN tasks ON employee_tasks.task_id = tasks.task_id
    """)
    tasks = cursor.fetchall()

    cursor.execute("""
    SELECT 
        employees.full_name,
        tasks.task_name,
        employee_tasks.status,
        employee_tasks.progress
    FROM employee_tasks
    JOIN employees ON employee_tasks.emp_id = employees.emp_id
    JOIN tasks ON employee_tasks.task_id = tasks.task_id
    """)
    assigned_tasks = cursor.fetchall()

    return render_template("admin_dashboard.html",
        task_count=task_count,
        employee_count=employee_count,
        employees=employees,
        tasks=tasks,
        assigned_tasks=assigned_tasks,
        pending=pending,
        in_progress=in_progress,
        completed=completed
    )


# ---------------- PROFILE ----------------
@app.route('/profile')
def profile():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT users.username, employees.full_name, employees.email
        FROM users
        JOIN employees ON users.userid = employees.userid
        WHERE users.userid = ?
    """, (session['userid'],))

    user = cursor.fetchone()
    return render_template("profile.html", user=user)


# ---------------- EDIT PROFILE ----------------
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        cursor.execute("""
            UPDATE employees 
            SET full_name=?, email=?
            WHERE userid=?
        """, (request.form['name'], request.form['email'], session['userid']))

        db.commit()
        return redirect('/profile')

    cursor.execute("SELECT full_name, email FROM employees WHERE userid=?", (session['userid'],))
    user = cursor.fetchone()

    return render_template("edit_profile.html", user=user)


# ---------------- CHANGE PASSWORD ----------------
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        cursor.execute("UPDATE users SET password=? WHERE userid=?",
                       (request.form['password'], session['userid']))
        db.commit()
        return redirect('/profile')

    return render_template("change_password.html")


# ---------------- ADD TASK ----------------
@app.route('/add_task', methods=['GET','POST'])
def add_task():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        cursor.execute(
            "INSERT INTO tasks(task_name,description,deadline) VALUES(?,?,?)",
            (request.form['name'], request.form['desc'], request.form['deadline'])
        )
        db.commit()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.execute("SELECT emp_id, full_name FROM employees")
    employees = cursor.fetchall()

    return render_template("add_task.html", tasks=tasks, employees=employees)


# ---------------- ASSIGN TASK ----------------
@app.route('/assign_task', methods=['GET', 'POST'])
def assign_task():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        emp_id = request.form['emp_id']
        task_id = request.form['task_id']

        cursor.execute("SELECT * FROM employee_tasks WHERE emp_id=? AND task_id=?", (emp_id, task_id))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO employee_tasks(emp_id, task_id) VALUES(?,?)", (emp_id, task_id))
            db.commit()

    cursor.execute("SELECT emp_id, full_name FROM employees")
    employees = cursor.fetchall()

    cursor.execute("SELECT task_id, task_name FROM tasks")
    tasks = cursor.fetchall()

    cursor.execute("""
        SELECT employee_tasks.id, employees.full_name, tasks.task_name,
               employee_tasks.status, employee_tasks.progress
        FROM employee_tasks
        JOIN employees ON employee_tasks.emp_id = employees.emp_id
        JOIN tasks ON employee_tasks.task_id = tasks.task_id
    """)
    assigned = cursor.fetchall()

    return render_template("assign_task.html", employees=employees, tasks=tasks, assigned=assigned)


# ---------------- EMPLOYEE DASHBOARD ----------------
@app.route('/employee')
def employee():
    if 'userid' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor()

    # Get employee id
    cursor.execute("SELECT emp_id FROM employees WHERE userid=?", (session['userid'],))
    emp = cursor.fetchone()

    if not emp:
        return redirect('/login')

    emp_id = emp[0]

    cursor.execute("SELECT username FROM users WHERE userid=?", (session['userid'],))
    username = cursor.fetchone()[0]

    cursor.execute("""
        SELECT t.task_name, t.description, t.deadline,
               et.progress, et.id, et.status
        FROM employee_tasks et
        JOIN tasks t ON et.task_id = t.task_id
        WHERE et.emp_id=?
    """, (emp_id,))

    tasks = cursor.fetchall()

    today = date.today()
    updated = []
    notifications = []

    for t in tasks:
        deadline = t[2]

        try:
            if deadline and isinstance(deadline, str):
                deadline = datetime.strptime(deadline,"%Y-%m-%d").date()
        except:
            deadline = None

        # Late check
        is_late = deadline and deadline < today and t[5] != 'completed'

        # Notifications
        if t[5] == "pending":
            notifications.append(f"New Task Assigned: {t[0]}")

        if deadline and (deadline - today).days == 1:
            notifications.append(f"Deadline Tomorrow: {t[0]}")

        updated.append(tuple(t) + (is_late,))

    return render_template(
        "employee_dashboard.html",
        tasks=updated,
        username=username,
        notifications=notifications
    )
# ---------------- UPDATE STATUS ----------------
@app.route('/update_status', methods=['POST'])
def update_status():
    db = get_db()
    cursor = db.cursor()

    status = request.form['status']
    progress = 100 if status == "completed" else 50 if status == "in_progress" else 0

    cursor.execute("UPDATE employee_tasks SET status=?, progress=? WHERE id=?",
                   (status, progress, request.form['id']))

    db.commit()
    return redirect('/employee')

# ---------------- MY TASKS ----------------
@app.route('/my_tasks')
def my_tasks():
    if 'userid' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT emp_id FROM employees WHERE userid=?", (session['userid'],))
    emp_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT t.task_name, t.description, t.deadline,
               et.status, et.progress
        FROM employee_tasks et
        JOIN tasks t ON et.task_id = t.task_id
        WHERE et.emp_id=?
    """, (emp_id,))

    tasks = cursor.fetchall()

    today = date.today()
    updated = []

    for t in tasks:
        deadline = t[2]

        if deadline:
            if isinstance(deadline, str):
                deadline = datetime.strptime(deadline, "%Y-%m-%d").date()

        is_late = deadline and deadline < today and t[3] != 'completed'

        updated.append((
            t[0],  # task name
            t[1],  # description
            t[2],  # deadline
            t[3],  # status
            t[4],  # progress
            t[3],  # status for filter
            is_late
        ))

    return render_template("my_tasks.html", tasks=updated)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/notifications')
def notifications():
    return redirect('/employee')


if __name__ == '__main__':
    app.run(debug=True)