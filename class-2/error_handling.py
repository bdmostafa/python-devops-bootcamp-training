# Basic Exception Handling
try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError as e:
    print(f"Error: {e}")


# Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))  # Could cause ValueError
    result = 10 / num  # Could cause ZeroDivisionError
except ValueError:
    print("❌ Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")


# Generic Exception Handling (Not Recommended)
try:
    # Some code
    print("This will cause an error")
except Exception as e:
    print(f"❌ An error occurred: {e}")


# Use finally to execute cleanup code, even if an error occurs.
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
finally:
    if 'file' in locals():
        file.close()  # Ensure file is closed
        print("✅ File closed successfully.")


# Use logging instead of print for better error tracking.
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    data = open("config.yaml").read()
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
    print("❌ Error logged to app.log")



# Exiting Gracefully with sys.exit(1)
# Exit script safely when a critical error occurs.
import sys

try:
    raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"❌ Critical Error: {e}")
    sys.exit(1)  # Exit with error status



# Practical Demo: Retry Failed Operations
import time

def read_file_with_retry(file_path, retries=3):
    for attempt in range(retries):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"❌ Attempt {attempt + 1}: File not found. Retrying...")
            time.sleep(2)  # Wait before retrying
    print("❌ Failed to read file after retries.")
    return None

content = read_file_with_retry("config.yaml")
