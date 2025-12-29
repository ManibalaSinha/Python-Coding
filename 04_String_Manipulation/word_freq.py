import re
from collections import Counter
def word_freq(text):
   words= re.findall(r'\b\w+\b', text.lower())
   return Counter(words)
print(word_freq("hi i am what i am"))
