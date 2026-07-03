from collections import Counter
def most_frequent(text):
    words = text.lower().split()
    counts = Counter(words)
    return counts.most_common(1)[0]
print(most_frequent(
    "python fastapi python react python"))
