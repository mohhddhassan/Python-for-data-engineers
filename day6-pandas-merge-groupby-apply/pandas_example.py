import pandas as pd

# Sample data
users = pd.DataFrame({
    "user_id": [1, 2],
    "name": ["Alice", "Bob"]
})

orders = pd.DataFrame({
    "order_id": [101, 102],
    "user_id": [1, 2],
    "amount": [250, 450]
})

# Merge
merged = pd.merge(users, orders, on="user_id", how="inner")
print("Merged Data:\n", merged)

# GroupBy
grouped = merged.groupby("user_id")["amount"].sum().reset_index()
print("\nGrouped (Total Amount):\n", grouped)

# Apply
merged["tax"] = merged["amount"].apply(lambda x: x * 0.1)
print("\nWith Tax Column:\n", merged)
