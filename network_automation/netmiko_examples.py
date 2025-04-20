# Monitoring Network Devices

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin123"
}

# Example 1: CPU Usage Check
net_connect = ConnectHandler(**device)
output = net_connect.send_command("show processes cpu")
print(output)
net_connect.disconnect()




# Example 2: Interface Status Check
output = net_connect.send_command("show ip interface brief")
print(output)


# Example 3: Ping Test
output = net_connect.send_command("ping 8.8.8.8")
print(output)


# Example 4: Logging & Alerting
with open("device_status.log", "a") as log:
    log.write(output)


