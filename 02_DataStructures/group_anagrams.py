from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())
print(group_anagrams(["eat","tea","ate", "tan","nat"]))