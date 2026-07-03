def word_freq(sentence):
    d = {}
    words = sentence.split()

    for w in words:
        d[w] = d.get(w, 0) + 1

    return d

print(word_freq("i love python and i love coding"))