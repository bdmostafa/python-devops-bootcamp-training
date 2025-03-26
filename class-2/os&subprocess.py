# Direct Execution (Not Recommended)
import os
os.system("ls -l")  # Linux/macOS
os.system("dir")  # Windows



# Safer Alternative (Recommended)
import subprocess
subprocess.run(["ls", "-l"])  # Linux/macOS
subprocess.run(["cmd", "/c", "dir"])  # Windows



print(os.environ)  # For all variables
print(os.environ.get("HOME"))  # Geting specific variable (Linux/macOS)
print(os.environ.get("USERNAME"))  # For Windows


print(os.getcwd())  # Current directory

print(os.listdir("."))  # Getting all info of current directory

print(os.listdir("/"))  # Getting all info of root directory


os.rename("old_name.txt", "new_name.txt")  # File delete
os.rename("old_folder", "new_folder")  # file rename

# def rename_file(origin, destination):
#     try:
#         os.rename(origin, destination)
#     except:
#         pass

# def rename(old, new):
#     stat = os.stat(old)
#     os.rename(old, new)
#     os.utime(new, (stat.st_atime, stat.st_mtime))
    
    
# Manage Processes & Services
# Restart nginx, apache, mysql
subprocess.run(["sudo", "systemctl", "restart", "nginx"])

# Check if the process is running
subprocess.run(["pgrep", "nginx"])


subprocess.run(["free", "-h"])  # Memory Usage
subprocess.run(["df", "-h"])  # Disk Usage

