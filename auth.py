import sys
import json
import os
from token_generator import token_user, load_token
from utils import load_fs, save_fs

fs = load_fs()
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
                    check_token = load_token()
                    if username not in check_token:
                        token = token_user(username)
                        return role, username,token
                    else:
                        token = "No token"
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
