from collections import Counter
def count_freq(lst):
   return dict(Counter(lst))
print(count_freq(['a','b','a']))
