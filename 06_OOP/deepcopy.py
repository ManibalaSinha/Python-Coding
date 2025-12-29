import copy
a = [[1,2], [3,4]]
b= copy.copy(a)
c= copy.deepcopy(a)
b[0].append(9)
print(a)
print(c)
print(b)