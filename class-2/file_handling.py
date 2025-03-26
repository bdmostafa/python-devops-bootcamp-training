# Opening a File

# open("filename", "mode")

# "r" → (Read Mode)
# "w" → (Write Mode)
# "a" → (Append Mode)
# "x" → (Exclusive Mode)


# Making a file and writing on it
file = open("testfile.txt", "w")  
file.write("Hello, DevOps Engineers!\n")  
file.write("This is a test file for file handling in Python.\n")  
file.close()  
print("File written successfully!")


# Reading from a file 
# read()
file = open("testfile.txt", "r")  
content = file.read()  
file.close()  
print("File Content:\n", content)


# readline()
file = open("testfile.txt", "r")

print(file.readline())   # 1st line reading  
print(file.readline())   # 2nd line reading  

file.close()

# readlines()
file = open("testfile.txt", "r")
lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()

# alternative use
with open("testfile.txt", "r") as file:
    for line in file:
        print(line.strip())  
        # every line reading and new line removing

# With 'with open()' we don't need to close the file

# Append to a file
with open("testfile.txt", "a") as file:
    file.write("Appending new content!\n")
print("New content added!")



# Deleting a File
# import os

# file_name = "testfile.txt"

# if os.path.exists(file_name):
#     os.remove(file_name)
#     print(f"{file_name} deleted successfully!")
# else:
#     print("File does not exist!")

import os

file_path = "/var/log/nginx/access.log"

if os.path.exists(file_path):
    print(f"{file_path} exists.")
    print(f"File name: {os.path.basename(file_path)}")
    print(f"Directory: {os.path.dirname(file_path)}")
else:
    print("File not found!")
    
    
    
# import shutil

# copy_file = "/var/log/nginx/access.log"
# backup_file = "/backup/access.log"
# old_backup_file = "/backup/nginx_access_old.log"

# # Copy a file
# if os.path.exists(copy_file):
#     shutil.copy(copy_file, backup_file)
#     print(f"{copy_file} copied to {backup_file}")
    
#     # Move a file
#     shutil.move(backup_file, old_backup_file)
#     print(f"{backup_file} moved to {old_backup_file}")
# else:
#     print("File not found!")


# import glob

# log_files = glob.glob("/var/log/nginx/*")

# if log_files:
#     for file in log_files:
#         print(file)
#         print(f"File name: {os.path.basename(file)}")
# else:
#     print("No log files found!")
    
    
    
from pathlib import Path

log_dir = Path("/var/log")

if log_dir.exists():
    print("Log directory exists.")

# Create a new directory
backup_dir = Path("/backup/logs")
backup_dir.mkdir(parents=True, exist_ok=True)

# Check if a specific log file exists
log_file = Path("/var/log/nginx/access.log")
if log_file.exists() and log_file.is_file():
    print("Nginx access log exists.")


