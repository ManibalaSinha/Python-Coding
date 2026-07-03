def two_sum(arr,target):
   l,r= 0, len(arr)-1
   while l<r:
      s= arr[l]+arr[r]
      if s== target:
         return [l,r]
      elif s<target:
         l+=1
      else:
         r-=1
print(two_sum([2,7,11,15],9))
      