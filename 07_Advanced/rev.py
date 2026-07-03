def rev(s):
    r=""
    for ch in s:
        r = ch + r
    return r
print(rev("rat"))