from collections import defaultdict
def group_ana(words):
   d= defaultdict(list)
   for w in words:
      d["".join(sorted(w))].append(w)
   return list(d.values())
print(group_ana(["tea","ate"]))