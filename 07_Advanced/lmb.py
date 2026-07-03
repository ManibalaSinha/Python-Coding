#Late binding in loops
funcs = []
for i in range(3):
    funcs.append(lambda: i)


print(funcs[0]())
print(funcs[1]())
print(funcs[2]())


#2