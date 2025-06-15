import paramiko
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# This script connects to multiple remote servers, collects system metrics (CPU, memory, disk usage),
# and pushes these metrics to a Prometheus Pushgateway.

# List of servers to connect to
servers = [
    {"host": "192.168.1.10", "user": "ubuntu", "key": "/path/to/private.key"},
    {"host": "192.168.1.11", "user": "ubuntu", "key": "/path/to/private.key"},
]

# Function to connect to a remote server and execute a command
def run_remote_command(host, user, key_path, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, key_filename=key_path)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    ssh.close()
    return output.strip()

# Function to collect metrics from a remote server
def collect_metrics(server):
    cpu_cmd = "top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'"
    mem_cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
    disk_cmd = "df -h / | awk 'NR==2{print $5}'"

    cpu = run_remote_command(server["host"], server["user"], server["key"], cpu_cmd)
    mem = run_remote_command(server["host"], server["user"], server["key"], mem_cmd)
    disk = run_remote_command(server["host"], server["user"], server["key"], disk_cmd)

    return {
        "host": server["host"],
        "cpu": float(cpu),
        "memory": float(mem),
        "disk": float(disk.strip('%'))
    }

    

def push_metrics_to_prometheus(metrics):
    registry = CollectorRegistry()
    cpu_gauge = Gauge('remote_cpu_usage', 'CPU usage', ['instance'], registry=registry)
    mem_gauge = Gauge('remote_memory_usage', 'Memory usage', ['instance'], registry=registry)
    disk_gauge = Gauge('remote_disk_usage', 'Disk usage', ['instance'], registry=registry)

    cpu_gauge.labels(metrics['host']).set(metrics['cpu'])
    mem_gauge.labels(metrics['host']).set(metrics['memory'])
    disk_gauge.labels(metrics['host']).set(metrics['disk'])

    push_to_gateway('http://localhost:9091', job='remote_metrics', registry=registry)

    
if __name__ == "__main__":
    for server in servers:
        metrics = collect_metrics(server)
        print(metrics)
        push_metrics_to_prometheus(metrics)
    try:
        print("Metrics pushed to Prometheus Pushgateway successfully.")
    except Exception as e:
        print(f"Failed to push metrics: {e}")
        # Handle the exception (e.g., log it, retry, etc.)
        pass
    
# Note: Ensure that the Prometheus Pushgateway is running and accessible at the specified URL.
# Ensure you have the required libraries installed:
# pip install paramiko prometheus_client
# Ensure you have the Prometheus Pushgateway running at http://localhost:9091
# Ensure you have SSH access to the remote servers with the provided credentials.
# Ensure the private key file has the correct permissions (e.g., chmod 600 /path/to/private.key)
# Ensure the remote commands are compatible with the target servers (e.g., Linux-based).
# Ensure the remote servers have the necessary tools installed (e.g., top, free, df).
# Ensure the Prometheus server is configured to scrape metrics from the Pushgateway.