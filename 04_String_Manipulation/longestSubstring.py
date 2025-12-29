def longest_substr(s):
   seen,result = {},""
   start=max_len=0
   for i, char in enumerate(s):
      if char in seen and seen[char]>=start:
         start=seen[char]+1
      seen[char]=i
      if i-start+1 > max_len:
         max_len= i-start+1
         result=s[start:i+1]
   return result
print(longest_substr("abcabcdr"))
                