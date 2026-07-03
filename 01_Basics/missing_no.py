def missing(arr,n):
   expected= n*(n+1)//2
   return expected - sum(arr)
print(missing([1,2,3,5],1))