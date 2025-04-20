from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin123"
}

# Step 1: Connect to a Cisco device using Netmiko
net_connect = ConnectHandler(**device)
print("Connected to device")


# Step 2: Pull current configuration
output = net_connect.send_command("show running-config")
print("Current Config:\n", output)


# Step 3: Push New Configuration (Change Hostname)
config_commands = ["hostname DevOps-Router"]
net_connect.send_config_set(config_commands)
print("Hostname changed")


# Step 4: Pull current configuration
import time

while True:
    interface_status = net_connect.send_command("show ip interface brief")
    print("Interface Status:\n", interface_status)
    time.sleep(60)  # wait 60 seconds before checking again



# Step 5: Auto logging
with open("interface_log.txt", "a") as f:
    f.write(interface_status + "\n")


# Step 6: Save the Configuration*
net_connect.save_config()

# *It can not be found after reboot, if it is not saved in memory 
