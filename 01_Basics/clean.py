data = [
    {"name": "A", "age": 25},
    {"name": "B", "age": None},
    {"name": "C"}]
cleaned = [    item for item in data
    if "age" in item and item["age"] is not None]
print(cleaned)
