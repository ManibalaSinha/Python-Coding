def length_longest_substring(s):
   seen= {}
   start = max_length =0
   for i, char in enumerate(s):
      if char in seen and seen[char]>= start:
         start = seen[char] +1
      seen[char]=i
      max_length = max(max_length, i- start +1)
   return max_length
print(length_longest_substring("abcab")) #3