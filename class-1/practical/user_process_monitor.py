import os
import subprocess

# Function to get the current logged-in user
def get_current_user():
    return os.getenv("USER") or os.getenv("USERNAME")

# Function to list all running processes
def get_running_processes():
    try:
        result = subprocess.run(["ps", "-e", "-o", "pid,comm"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error fetching process list: {e}")
        return None

# Function to check if a critical process is running
def check_critical_process(process_name):
    process_list = get_running_processes()
    if process_list and process_name in process_list:
        print(f"✅ {process_name} is running!")
    else:
        print(f"❌ WARNING: {process_name} is NOT running!")

# Function to save process list to a file
def save_process_list_to_file():
    processes = get_running_processes()
    if processes:
        with open("process_list.txt", "w") as file:
            file.write(processes)
        print("📄 Process list saved to process_list.txt")

# Main Execution
if __name__ == "__main__":
    print(f"🔹 Logged-in User: {get_current_user()}")
    
    print("\n🔹 Checking Critical Processes...")
    check_critical_process("sshd")  # SSH Daemon (Change if needed)
    check_critical_process("nginx")  # Web Server (Change if needed)
    
    print("\n🔹 Saving Process List to File...")
    save_process_list_to_file()
