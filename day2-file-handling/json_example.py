import json

data = {"id": 1, "name": "Alice"}

# Writing JSON
with open('user.json', 'w') as f:
    json.dump(data, f)

# Reading JSON
with open('user.json', 'r') as f:
    user = json.load(f)
    print(user)
