def char_freq(s):
    # Fill code here
    char_freq={}
    for ch in s:
        char_freq[ch]= char_freq.get(ch,0)+1
    return char_freq
    pass

print(char_freq("banana"))