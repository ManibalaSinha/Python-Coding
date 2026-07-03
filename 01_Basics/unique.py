def uniq(s):
   start,max_len=0
   seen={}
   for i,ch  in enumerate(s):
      if ch in seen and seen [ch] i>=start:
         start= seen[ch]
      seen[ch]=i 
      max_len=max(max_len,i-start+1)
   return max_len

