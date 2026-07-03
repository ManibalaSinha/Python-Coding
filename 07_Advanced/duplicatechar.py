def duplicates(s):
    freq = {}
    dup = []

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in freq:
        if freq[ch] > 1:
            dup.append(ch)

    return dup

print(duplicates("programming"))