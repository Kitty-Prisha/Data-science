import numpy as np
arr=np.array([[1,2,3,4,5],[1,2,6,5,0],[2,5,7,8,9]])
print(arr)
print(arr.shape)
newarr=arr.reshape(5,3)
print(newarr)