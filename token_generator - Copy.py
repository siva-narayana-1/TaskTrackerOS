import os
import random
import json
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
    