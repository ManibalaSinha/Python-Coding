import numpy as np
arr = np.array([1,2,3,4]) #fast numeric array
arr * 2 #multiply each element by 2
arr[arr > 2] #filter values greater than 2, result [3,4]
np.mean(arr) #calculate average, result 2.5
np.where(arr > 2, arr, 0) #if value>2->keep value,else replaces with 0, result [0,0,3,4]
#filter data, handle nulls, group aggregate, conditions
 