def balance(transactions):
   balance={}
   for t in transactions:
      user = t["user"]
      amt = t["amount"]
      balance["user"] = balance.get(user,0)+ amt
   return balance

transactions = [
    {"user": "A", "amount": 100},
    {"user": "B", "amount": 200},
    {"user": "A", "amount": -50},
    {"user": "B", "amount": -100},
    {"user": "C", "amount": 300}
]
print(balance(transactions))