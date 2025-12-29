def replace_consonants(text, replacement):
    vowels = "aeiouAEIOU"
    return "".join([replacement if char.isalpha() and char not in vowels else char for char in text])

# Example
text = "Hello World"
new_text = replace_consonants(text, "#")
print("Replace consonants:", new_text)
