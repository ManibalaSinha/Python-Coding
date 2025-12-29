def is_palin(s):
   s=s.lower().replace(" ", "")
   return s==s[::-1]
print(is_palin("mamam"))