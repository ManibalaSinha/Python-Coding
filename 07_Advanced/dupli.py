nums = [1,2,2,3]
seen=set()
dup=set()
for x in nums:
    if x in seen:
        dup.add(x)
    seen.add(x)
print(dup)