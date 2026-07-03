def find_duplicates(lst):
    # Fill code here
    freq ={}
    dup=[]
    for ch in lst:
        freq[ch] = freq.get(ch,0) +1
        
    for ch in freq:
        if freq[ch] > 1:
            dup.append(ch)
    return dup
    pass

print(find_duplicates([1,2,3,2,4,5,1]))