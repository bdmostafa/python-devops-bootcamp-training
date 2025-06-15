import logging
from pythonjsonlogger import jsonlogger
import random

logger = logging.getLogger()
logHandler = logging.StreamHandler()
logHandler = logging.FileHandler('app.log')  # adjust path as needed

# Rich log format
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s %(user)s')

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)  # capture all levels

# # === Log Examples ===

# INFO
logger.info("User login successful", extra={"user": "mostafa"})

# DEBUG
logger.debug("Fetching user preferences", extra={"user": "mostafa"})

# WARNING
logger.warning("Password expires in 3 days", extra={"user": "mostafa"})

# ERROR (Simulated exception)
try:
    result = 10 / random.choice([0, 1])
except ZeroDivisionError as e:
    logger.error("Division by zero error occurred", extra={"user": "mostafa"})

# CRITICAL
logger.critical("Unauthorized admin access attempt detected", extra={"user": "hacker"})

# Custom Function Example
def simulate_user_action(user):
    logger.info("User accessed dashboard", extra={"user": user})
    logger.debug("User clicked settings", extra={"user": user})
    try:
        if random.choice([True, False]):
            raise ValueError("Simulated backend failure")
    except ValueError as ve:
        logger.error(f"Application error: {str(ve)}", extra={"user": user})

simulate_user_action("mostafa")
simulate_user_action("guest_user")