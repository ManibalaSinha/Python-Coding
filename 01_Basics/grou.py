from collections import defaultdict
def group_anagram(words):
   d= defaultdict(int)
   for w in words:
      d["".join(sorted(w))].append(w)
   return list(d.values())