from collections import defaultdict
def group_anagram(words):
   d= defaultdict(list)
   for w in words:
      d[''.join(sorted(w))].append(w)
   return list(d.values())
print(group_anagram(["eat","tea","ate", "tan","nat"]))