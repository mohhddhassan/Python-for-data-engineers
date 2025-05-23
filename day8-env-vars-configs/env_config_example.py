import os
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
print(f"DB Credentials: {user} / {password}")

# Load YAML config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print(f"DB Host: {config['database']['host']}")
