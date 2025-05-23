import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Cannot divide by zero: {e}")
        return None

logging.info("Starting division task")
result = divide(10, 0)
logging.info(f"Result: {result}")
