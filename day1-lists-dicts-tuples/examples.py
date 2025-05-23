# List
pipeline_steps = ["extract", "transform", "load"]
pipeline_steps.append("validate")
print(pipeline_steps)

# Dict
user_map = {"101": "Alice", "102": "Bob"}
print(user_map.get("101"))

# Tuple
db_config = ("localhost", 5432)
print(f"Connecting to {db_config[0]} on port {db_config[1]}")
