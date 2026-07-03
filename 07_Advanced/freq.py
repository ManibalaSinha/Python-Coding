def char_freq(s):
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d

print(char_freq("banana"))