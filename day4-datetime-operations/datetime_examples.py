from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now)

past = now - timedelta(days=7)
print("1 week ago:", past)

# Format datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Parse string to datetime
dt = datetime.strptime("2024-05-10", "%Y-%m-%d")
print("Parsed:", dt)
