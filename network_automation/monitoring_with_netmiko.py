# Step 1: Setup and Connect

from netmiko import ConnectHandler
import time
import smtplib
from email.message import EmailMessage

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin123"
}

try:
    net_connect = ConnectHandler(**device)
except Exception as e:
    print("Connection failed:", e)


# Step 2: Fetch interface stats every X seconds

def monitor_interface(interval=30):
    while True:
        output = net_connect.send_command("show ip interface brief")
        print("Interface Snapshot:\n", output)
        time.sleep(interval)
        
        lines = output.splitlines()  # Split outputs line by line

        print("\n Active Interfaces:")
        print("=" * 40)

        for line in lines:
            # SKip 1st line because of header
            if "Interface" in line:
                continue

            # If both Status and Protocol are Up
            if "Up" in line:
                print(line)

        print("=" * 40)
        time.sleep(interval)

# Step 3: CPU/Memory Usage Check & Alert

def check_cpu_memory():
    cpu = net_connect.send_command("show processes cpu | include CPU utilization")
    memory = net_connect.send_command("show processes memory | include Processor Pool")

    print("CPU Usage:\n", cpu)
    print("Memory Status:\n", memory)

    if "90%" in cpu:
        send_email_alert("High CPU usage detected!", cpu)



# Step 4: Email Alert Function

def send_email_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "monitor@network.com"
    msg['To'] = "admin@yourcompany.com"

    with smtplib.SMTP('smtp.yourmail.com', 587) as server:
        server.starttls()
        server.login("monitor@network.com", "yourpassword")
        server.send_message(msg)
        print("Alert email sent!")


# Step 5: Run Everything

monitor_interface()

# Or calling check_cpu_memory() we can periodic
# check_cpu_memory()