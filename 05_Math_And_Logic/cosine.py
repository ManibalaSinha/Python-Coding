import re
import math
from collections import Counter

def cosine_similarity(s1, s2):
    # Tokenize into lowercase words only
    w1 = Counter(re.findall(r'\b\w+\b', s1.lower()))
    w2 = Counter(re.findall(r'\b\w+\b', s2.lower()))

    # Union of all unique words
    all_words = set(w1.keys()) | set(w2.keys())

    # Compute dot product and magnitudes
    dot = sum(w1[w] * w2[w] for w in all_words)
    mag1 = math.sqrt(sum(v*v for v in w1.values()))
    mag2 = math.sqrt(sum(v*v for v in w2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return round(dot / (mag1 * mag2), 3)

print(cosine_similarity("AI models learn from data", "AI systems train on data"))
