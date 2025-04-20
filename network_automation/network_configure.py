from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin123"
}

net_connect = ConnectHandler(**device)

# interface configuration
config_commands = [
    "interface GigabitEthernet0/1",
    "description Connected to Core Switch",
    "ip address 10.0.0.1 255.255.255.0",
    "no shutdown"
]

output = net_connect.send_config_set(config_commands)
print(output)

net_connect.disconnect()


# routing configuration
routing_commands = [
    "router ospf 1",
    "network 10.0.0.0 0.0.0.255 area 0"
]

net_connect.send_config_set(routing_commands)



# Firmware upgrade (TFTP Setup)
upgrade_commands = [
    "copy flash: tftp://192.168.1.2/cisco_ios_15.2.2.bin",
    "y"
]

firmware_update = [
    "copy tftp://192.168.1.100/new-ios.bin flash:",
    "reload"
]

net_connect.send_config_set(firmware_update)

