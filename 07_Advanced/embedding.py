def simple_embedding(words):
    embeddings = {}
    for word in words:
        # simple vector = count of letters a-z
        vector = [0]*26
        for ch in word.lower():
            if ch.isalpha():
                vector[ord(ch)-97] += 1
        embeddings[word] = vector
    return embeddings

print(simple_embedding(["AI", "Data"]))
