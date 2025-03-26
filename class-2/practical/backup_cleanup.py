# Automating File Backups & Cleanup
# Problem: Old logs and temporary files fill up disk space.
# Solution: Use Python to delete old files and back up important ones.

import os
import shutil
import time

backup_dir = "/backup/"
source_dir = "/var/logs/"
timestamp = time.strftime("%Y%m%d")

shutil.copytree(source_dir, backup_dir + timestamp)
print("Backup completed!")

