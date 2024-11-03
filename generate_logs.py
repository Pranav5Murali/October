# generate_logs.py

import os
from datetime import datetime

# Define the log directory and file path
log_dir = "/home/pranav/Documents/Test"
os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Create a log file with the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(log_dir, f"log_{timestamp}.txt")

# Write some content to the log file
with open(log_file_path, "w") as log_file:
    log_file.write(f"Log created on {timestamp}\n")
    log_file.write("This is a test log file.\n")

print(f"Log file created at {log_file_path}")
