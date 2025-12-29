def solution(A,k):
   n= len(A)
   if n==0:
      return A
   k= k%n #ruduce unnecessary rotation
   return A[-k:] + A[:-k] # lastk + first (n-k) elements
A=[3,76,13,2,9]
k=3
print(solution(A,k))