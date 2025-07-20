import re
from functools import wraps
import logging

VALID_INPUT_PATTERN = re.compile(r'^(greater|less)$', re.IGNORECASE)

# Decorator to log when a function is called
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Returns a nested function to double a base reward value
def reward_multiplier():
    base = 20
    def double():
        nonlocal base # Allows the nested function to modify the var from the enclosing scope
        base *= 2
        return base
    return double
