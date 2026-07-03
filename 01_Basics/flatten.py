def flatten(data, parent="", result=None):
    if result is None:
        result = {}
    for key, value in data.items():
        new_key = f"{parent}.{key}" if parent else key
        if isinstance(value, dict):
            flatten(value, new_key, result)
        else:
            result[new_key] = value
    return result
data = {
    "user": {
        "address": {
            "city": "Toronto" } }}
print(flatten(data))
