from collections import Counter
def uniq(s):  
   count = Counter(s)
   for ch in s:
      if count[ch] == 1:      
         return ch
   return None
print(uniq("abcdcd"))

