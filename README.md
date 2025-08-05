# 🖥️ TaskTrack OS - A CLI-based Role-Oriented Task Manager

TaskTrack OS is a Python-based Command Line Interface (CLI) task management system that simulates a lightweight operating system environment with **role-based access control**, **persistent user authentication**, and **task tracking functionality** — all without using external libraries.

---

## ✨ Features

- 🔐 User Signup & Login with role-based access (`admin` / `user`)
- ✅ Task creation and viewing (user-specific)
- 📂 Persistent storage via file handling and JSON
- 🎭 Role-based dashboards (admin/user)
- 🧪 Modular code with `auth`, `task`, `token`, and `main` scripts
- ⌨️ Clean CLI interaction using standard input/output

---

## 🗂️ Project Structure

TaskTrack-OS/
'''|'''
'''├── main.py # Entry point, CLI routing'''
'''├── auth.py # User login/signup and filesystem loader'''
'''├── task.py # Add, view (and later edit/delete) tasks'''
'''├── token.py # (Optional) Handles token/session logic (in progress)'''
'''├── users.json # Stores user data by role'''
'''├── task.json # Stores user-task mapping'''
'''├── token.json # Stores token/session info (optional feature)'''
