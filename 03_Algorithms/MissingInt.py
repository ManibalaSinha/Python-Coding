def solution(A):
   n=len(A)
   present = [False] * (n+2)
   for x in A:
      if 1 < x <= n+1:
         present[x] =True
   for i in range(1, n+2):
      if not present[i]:
         return i
      
A=[1,5,3,9]
n=6
print(solution(A))