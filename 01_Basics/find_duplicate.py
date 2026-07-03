def find_duplicates(transactions):
   seen=set()
   duplicates=[]
   for t in transactions:
      key=(t["user"],t["amount"])#fixed
      if key in seen:
         duplicates.append(key)
      else:
         seen.add(key)#fixed
   return duplicates
transactions = [
    {"user": "A", "amount": 100},
    {"user": "B", "amount": 200},
    {"user": "A", "amount": 100},  
]# duplicate
print(find_duplicates(transactions))
      