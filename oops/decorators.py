import logging
from functools import wraps
import sys
import traceback

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_function_call(func):
    """A decorator to log function calls, arguments, and return values."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log before the function runs
        logger.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        
        try:
            # Call the original function
            result = func(*args, **kwargs)
            # Log after the function runs successfully
            logger.info(f"Function '{func.__name__}' returned: {result}")
            return result
        except Exception as e:
            # Log any exceptions
            logger.error(f"Exception in '{func.__name__}': {e}", exc_info=True)

            # Capture exception info
            exc_info_tuple = sys.exc_info()
            error_type, error_instance, traceback_obj = exc_info_tuple
            logger.error(f"Error Type: {error_type}; Error Message: {error_instance}; Traceback Object: {traceback_obj}")
           
           # Format the traceback details
            error_details = traceback.format_exc()
            custom_message = f"*** UNEXPECTED FAILURE ***\n{error_details}"
            logger.error(custom_message)
            raise
            
    return wrapper

# Example usage:

@log_function_call
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

@log_function_call
def divide_numbers(a, b):
    """Divides two numbers, handles potential ZeroDivisionError."""
    return a / b

if __name__ == "__main__":
    add_numbers(5, 3)
    divide_numbers(10, 0)
    try:
        divide_numbers(10, 0)
    except ZeroDivisionError:
        pass
