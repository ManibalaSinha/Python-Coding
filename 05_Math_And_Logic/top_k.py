from collections import Counter
import heapq
def top_k_frequent(nums, k):
   freq = Counter(nums)#count how many times each element occurs
   return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
print(top_k_frequent([1,1,1,2,2,2,3,3,3,40,3],2))
   