import os
import json

task_file = "task.json"
task = {}
def load_task():
    global task
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            task = json.load(f)
    else:
        task = {}
    return task

def save_task():
    with open(task_file, "w") as f:
        json.dump(task, f, indent=4)

def add(username):
    task_name = input("Enter your task: ")
    priority = input("High/Low: ").lower()
    if username not in task:
        task[username] = {}
    if task_name in task[username]:
        return "Task already exists for this user."
    else:
        task[username][task_name] = priority
        save_task()
        return f"Task '{task_name}' added for {username} with {priority} priority."
def view(username):
    if username in task:
        user_tasks = task[username]
        if not user_tasks:
            return "No tasks found."
        for name, prio in user_tasks.items():
            print(f"- {name} [{prio}]")
    else:
        return "No tasks for this user."
load_task()

