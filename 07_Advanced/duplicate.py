nums=[1,2,2,3]
dup=set([x for x in nums if nums.count(x)>1])
print(dup)