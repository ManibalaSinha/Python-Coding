import re
def tokenize(text):
   return re.findall(r"\w+|[^\w\s]", text)
print(tokenize("AI, data, and Python — they're all connected!"))
print(tokenize("ai data hi "))