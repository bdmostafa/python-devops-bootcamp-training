import time
import random

LOG_FILE = "app.log"

# Sample log messages
info_messages = [
    "App started",
    "User logged in",
    "File uploaded",
    "Scheduled job executed",
    "Connection established"
]

warning_messages = [
    "High memory usage",
    "Disk usage above threshold",
    "API response slow",
    "Temporary network issue"
]

error_messages = [
    "Failed to connect to database",
    "Timeout while calling external API",
    "Unhandled exception occurred",
    "File not found"
]

def write_log():
    with open(LOG_FILE, "a") as f:
        log_type = random.choice(["INFO", "WARNING", "ERROR"])
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if log_type == "INFO":
            message = random.choice(info_messages)
        elif log_type == "WARNING":
            message = random.choice(warning_messages)
        else:
            message = random.choice(error_messages)

        log_line = f"[{log_type}] {timestamp} {message}\n"
        f.write(log_line)
        print("Log written:", log_line.strip())

if __name__ == "__main__":
    for _ in range(10):  # generate 10 log lines
        write_log()
        time.sleep(1)
