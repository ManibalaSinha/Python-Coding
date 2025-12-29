from collections import defaultdict
def flag_users(transactions):
   count = defaultdict(int)
   flagged = set()
   for user, amt in transactions:
      if amt > 1000:
         count[user] += 1
      if count[user] >= 3:
         flagged.add(user)
   return list(flagged)
transactions = [(1,1500),(2,2500), (2,1500),(2,1800),(3,1200),(3,1300),(3,1400)]
print(flag_users(transactions))
