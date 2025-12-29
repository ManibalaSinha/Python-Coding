def replace_vowels(text, replacement):
    vowels = "aeiouAEIOU"
    return "".join([replacement if char in vowels else char for char in text])

# Example
text = "Hello World"
new_text = replace_vowels(text, "*")
print("Replace vowels:", new_text)
