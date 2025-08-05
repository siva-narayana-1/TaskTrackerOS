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
|

├── main.py # Entry point, CLI routing

├── auth.py # User login/signup and filesystem loader

├── task.py # Add, view (and later edit/delete) tasks

├── token.py # (Optional) Handles token/session logic (in progress)

├── users.json # Stores user data by role

├── task.json # Stores user-task mapping

├── token.json # Stores token/session info (optional feature)



---

## 📄 File Descriptions

| File/Module     | Description |
|----------------|-------------|
| `main.py`      | 🧠 The central CLI app that handles login, signup, and user/admin dashboard routing. This is the entry point of the project. |
| `auth.py`      | 🔐 Handles user authentication — login, signup, and user-role management. Uses `users.json` for storing registered users. |
| `task.py`      | ✅ Manages task operations like `add` and `view`. Each user’s tasks are stored in `task.json` with associated priorities. |
| `token.py`     | 🔄 (Optional/in-progress) Module to manage token-based session authentication or future features like login sessions or password resets. |
| `users.json`   | 📂 JSON file that stores user credentials grouped by roles (`admin`, `user`). Created dynamically via `auth.py`. |
| `task.json`    | 📋 Stores per-user tasks in key-value format: `{ username: { task: priority } }`. Created dynamically by `task.py`. |
| `token.json`   | 🧾 (Optional) Placeholder for session or token-related info. Planned for features like session timeout or secure auth. |

---

