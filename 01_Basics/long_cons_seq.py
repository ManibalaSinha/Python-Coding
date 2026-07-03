def long_cons_seq(nums):
   num_set = set(nums)
   max_len = 0
   for num in num_set:
      if num -1 not in num_set:
         current = num
         length = 1
         while current + 1 in num_set:
            current+=1
            length+=1
         max_len=max(max_len,length)
   return max_len
print(long_cons_seq([7,6,5]))