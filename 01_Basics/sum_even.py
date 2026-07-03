def sum_even(lst):
   return sum(x for x in lst if x%2==0)
print(sum_even([2,4,6]))