data = [    {"name": "Alice", "score": 80},
    {"name": "Bob", "score": 90},
    {"name": "Alice", "score": 70}]

from collections import defaultdict
scores = defaultdict(list)
for item in data:
    scores[item["name"]].append(item["score"])
result = {name: sum(v)/len(v) for name, v in scores.items()}
print(result)
