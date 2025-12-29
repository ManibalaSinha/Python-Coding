stopwords = {'the', 'is', 'in', 'and', 'to', 'a', 'of'}

def count_stopwords(text):
    words = text.lower().split()
    return sum(1 for w in words if w in stopwords)

print(count_stopwords("The AI model is in the data pipeline"))
