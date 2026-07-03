words = ["apple", "ant", "banana", "ball"]
grouped = {}
for word in words:   
   key = word[0]
   grouped.setdefault(key,[]).append(word)
print(grouped)