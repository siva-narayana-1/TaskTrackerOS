import sys
import json
import os
from token_generator import token_user
fs_file = "fs.json"
fs = {}

def load_fs():
    global fs
    if os.path.exists(fs_file):
        with open(fs_file, "r") as f:
            fs = json.load(f)
    else:
        fs = {}
    return fs

def save_fs():
    with open(fs_file, "w") as f:
        json.dump(fs, f, indent=4)

def signup():
    try:
        username = input("Choose a username: ")
        password = input("Enter a password: ")
        role = input("Enter your role (admin/user): ")

        if role in fs:
            if username in fs[role]:
                print(f"{username} is already taken.")
                return None
            else:
                fs[role][username] = password
        else:
            fs[role] = {username: password}

        save_fs()
        print(f"{username} registered successfully as {role} ✅")
        print("Logging you in automatically...\n")
        token = token_user(username)
        return role, username, token

    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at line {exc_line.tb_lineno} as {exc_msg}")
        return None

def login():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for role in fs:
            if username in fs[role]:
                if fs[role][username] == password:
                    token = token_user(username)
                    return role, username, token
                else:
                    print("Incorrect password.")
                    return None

        print(f"{username} is incorrect. Please check once.")
        return None

    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at line {exc_line.tb_lineno} as {exc_msg}")
        return None
