# Nginx configuration file path
CONFIG_FILE = "nginx.conf"

# New values to update
NEW_WORKER_PROCESSES = 4
NEW_LISTEN_PORT = 8080
NEW_DOCUMENT_ROOT = "/var/www/html"
ENABLE_GZIP = True  # Enable or disable gzip

# Function to update nginx.conf file
def update_nginx_config():
    try:
        # Read the original file content
        with open(CONFIG_FILE, "r") as file:
            lines = file.readlines()

        # Modify the necessary configurations
        with open(CONFIG_FILE, "w") as file:
            for line in lines:
                # Update worker_processes
                if "worker_processes" in line:
                    line = f"worker_processes {NEW_WORKER_PROCESSES};\n"
                
                # Update listen port
                elif "listen" in line and "server" in "".join(lines):
                    line = f" listen {NEW_LISTEN_PORT};\n"
                
                # Update document root
                elif "root" in line and "/usr/share/nginx/html" in line:
                    line = f" root {NEW_DOCUMENT_ROOT};\n"

                # Enable gzip compression
                elif "gzip " in line and ENABLE_GZIP:
                    line = " gzip on;\n"

                file.write(line)

        print("✅ Nginx configuration updated successfully!")

    except Exception as e:
        print(f"❌ Error updating nginx.conf: {e}")

# Run the function
update_nginx_config()
