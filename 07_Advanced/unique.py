def first_unique(s):
    # Fill code here
    first_unique = {}
    for ch in s:
       first_unique[ch] = first_unique.get(ch,0) + 1
    for ch in s:
       if first_unique[ch] == 1: 
         return ch
    return None
    pass

print(first_unique("swiss"))