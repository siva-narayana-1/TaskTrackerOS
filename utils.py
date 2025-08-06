import json
import os
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