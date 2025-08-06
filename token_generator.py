import random
import json
from utils import load_fs
import os
file_name = "token.json"
token = {}
def load_token():
    global token
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            token = json.load(f)
    else:
        return "{file_name} not found"
    return token
def save():
    with open(file_name, "w") as f:
        json.dump(token, f, indent=4)

def token_user(username):
    username = username
    token_number = username+str(random.randint(0,9))
    token[username] = token_number
    save()
    return token_number

def remove_token(username):
    if username in token:
        token.pop(username)
        save()
        return "users loged out."
    else:
        return "No user found."
    
def view_logged(username):
    if username in token:
        for user in token.keys():
            print(f"--- {user}")

def remove_locked_user(username,role):
    check_user = load_fs()
    if username in token:
        user = input(f"Enter {token} names only to delete:")
        if user in token and user in check_user["user"]:
            token.pop(user)
            save()
            print(f"{user} is unLocked.")
        else:
            print("user not available.")