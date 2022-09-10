import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([range(1,3)])
array3 = np.array([i for i in range(1,3)])
array4 = np.array([i ** 2 for i in range(1,10)])
sum_array4 = np.array([sum(array4)])

print(array1)
print(array2)
print(array3)
print(array4)
print(sum_array4)

# you can treat vectors as arrays

vector1 = np.array([1,0,0])
vector2 = np.array([0,1,0])

print(np.dot(vector1,vector2))
m1 = np.array([[1.0,2.0],# be sure to use floats for accuracy
               [2.0,1.0]])
print(m1[0,1])# index like a list
print(m1)
#done
