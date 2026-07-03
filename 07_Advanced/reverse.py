def reverse_string(s):
    # Fill code here
    rev=""
    for ch in s:
        rev = ch + rev 
    return rev
    pass

print(reverse_string("synechron"))