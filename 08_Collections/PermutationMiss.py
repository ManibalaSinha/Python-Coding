def solution(A):
   n=len(A)+1 #total numbers including missing one
   return n*(n+1) // 2 -sum(A) #sum 0f 1..N+1
A=[2,3,1,5]
print(solution(A))