from  collections import Counter
def most_freq_char(s:str) -> str:
   count = Counter(s.replace(" ",""))
   return count.most_common(1)[0][0]
print(most_freq_char("st bring hhhhsd"))