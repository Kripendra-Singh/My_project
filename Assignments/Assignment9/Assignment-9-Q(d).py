import numpy as np
arr=np.array([[1,2,3,4],
              [2,3,2,1],[12,13,14,11]])
l,r=arr.shape
print("\n minimum element of given array is:",arr.min())
print("\n maximum element of given array is:",arr.max())
print(f"\n number of rows are {l} and columns are {r} of given array are:\n",l)
# Specific element
print("\nElement at [1,2]:\n", arr[1, 2])

k=arr.sum()
print("\nsum of array\n",k)
print("\n arithmatic operation on array are\n")
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print("Addition:\n", x + y)
print("Subtraction:\n", x - y)
print("Multiplication:\n", x * y)
print("Division:\n", x / y)