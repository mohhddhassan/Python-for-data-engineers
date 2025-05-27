# -------------------------
# 1️⃣ List: Sequence of Steps
# -------------------------
# A list is like a collection of items, you can add, remove, and access them.
pipeline_steps = ["extract", "transform", "load"]

# Add a new step at the end
pipeline_steps.append("validate")

# Add a new step at the beginning (position 0)
pipeline_steps.insert(0, "ingest")

# Add more steps at once
pipeline_steps.extend(["monitor", "alert"])

# Print the whole list
print("Pipeline steps:", pipeline_steps)

# Access specific items in the list
print("First step:", pipeline_steps[0])  # First item
print("Last two steps:", pipeline_steps[-2:])  # Last two items

# -------------------------
# 2️⃣ Dictionary: Key-Value Pairs
# -------------------------
# A dictionary is like a lookup table where you search with a key.
user_map = {"101": "Alice", "102": "Bob"}

# Add a new user
user_map["103"] = "Charlie"

# Access a user's name by their ID
print("User 101:", user_map.get("101"))  # Output: Alice
print("User 103:", user_map.get("103", "User not found"))  # Default message if key not found

# Print all users' names
print("All users:", list(user_map.values()))

# -------------------------
# 3️⃣ Tuple: Fixed Collection of Items
# -------------------------
# A tuple is like a list, but you can't change it (immutable).
db_config = ("localhost", 5432, "admin", "password")

# Access values by position
print(f"Connecting to {db_config[0]} on port {db_config[1]} as user '{db_config[2]}'")

# Unpack tuple values into variables
host, port, user, password = db_config
print(f"Host: {host}, Port: {port}, User: {user}, Password: {password}")

# -------------------------
# 🎓 What You Should Remember:
# -------------------------
# ✅ List: Ordered collection, changeable (add, remove)
# ✅ Dictionary: Key-value mapping (like a phonebook)
# ✅ Tuple: Ordered collection, but unchangeable
