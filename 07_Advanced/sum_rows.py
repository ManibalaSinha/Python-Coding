import numpy as np

a = np.arange(6).reshape(2,3)
# Print row-wise sum
#a=([0,1,2],[3,4,5])
print(a.sum(axis=1))