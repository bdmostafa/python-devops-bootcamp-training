# Problem: Old log files are filling up the server's storage
# Solution: Use a Python script to remove old log files and back them up

import os
import shutil

log_dir = "/var/logs"
backup_dir = "/backup"

for file_name in os.listdir(log_dir):
    if file_name.endswith(".log"):
        shutil.move(log_dir + file_name, backup_dir + file_name)
        print(f"Moved {file_name} to backup!")
