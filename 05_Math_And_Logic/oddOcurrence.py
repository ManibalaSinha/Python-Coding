def solution(A):
   result=0
   for num in A:
      result ^= num #XOR cancels out pair

   return result
A=[9,3,9,3, 9,7,9]
print(solution(A))