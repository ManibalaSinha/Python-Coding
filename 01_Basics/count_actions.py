from collections import Counter
def count_actions(logs):
   return Counter(log["user"] for log in logs)
logs=[{"user":"A"},{"user":"B"},{"user":"A"}]
print(count_actions(logs))