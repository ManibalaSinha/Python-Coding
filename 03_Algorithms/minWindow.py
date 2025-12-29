from collections import Counter

def minWindow(s, t):
    need, missing = Counter(t), len(t)   # what we need, and how many chars are missing
    i = start = end = 0                  # sliding window left pointer, result range
    for j, c in enumerate(s, 1):         # right pointer moves forward (1-based index j)
        if need[c] > 0:                  # if this char is still required
            missing -= 1                 # one less missing
        need[c] -= 1                     # consume one occurrence of this char

        # if all characters are found (missing == 0)
        if missing == 0:
            # shrink the left side while it's "extra" chars
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1

            # update result if smaller window is found
            if end == 0 or j - i < end - start:
                start, end = i, j

    return s[start:end]
