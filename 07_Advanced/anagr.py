def is_anagram(s1, s2):
    # Fill code here
    if len(s1)!=len(s2):
        return False
    freq1={}
    freq2={}
    for ch in s1:
        freq1[ch]= freq1.get(ch,0) +1
  
    for ch in s2:
        freq2[ch] = freq2.get(ch,0)+1
   
    return freq1 == freq2

    pass

print(is_anagram("listen","silent"))