data = {
    "users": [
        {"name": "A", "orders": [100, 200]},
        {"name": "B", "orders": [50]}   ]}
result = {}
for user in data["users"]:
    result[user["name"]] = sum(user["orders"])
print(result)
#Output:{'A': 300, 'B': 50}