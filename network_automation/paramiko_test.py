import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.1.10", username="admin", password="admin123")

stdin, stdout, stderr = ssh.exec_command("show ip interface brief")
print(stdout.read().decode())

ssh.close()
