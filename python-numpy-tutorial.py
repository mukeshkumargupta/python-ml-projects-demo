##Very good reference for tutorial

##refrence Very good tutorial first practic fron : https://docs.scipy.org/doc/numpy/user/quickstart.html
##Reference:Then practive from link http://cs231n.github.io/python-numpy-tutorial/
import os
import numpy as np
a = np.arange(15).reshape(3, 5)

print (a)

#array([[ 0,  1,  2,  3,  4],
 #      [ 5,  6,  7,  8,  9],
 #      [10, 11, 12, 13, 14]])
print (a.shape)
#(3, 5)
print (a.ndim)
#2
print (a.dtype.name)
#'int64'  ##it varies on os 32 could be like on window 8 coming 32
print (a.itemsize)
#8    ##it varies on os 32 could be like on window 8 coming 4
print (a.size)
#15
print (type(a))
#<type 'numpy.ndarray'>
b = np.array([6, 7, 8])
print (b)
#array([6, 7, 8])
print (type(b))
#<type 'numpy.ndarray'>


b = np.array([(1.5,2,3), (4,5,6)])
print (b)
#array([[ 1.5,  2. ,  3. ],
#      [ 4. ,  5. ,  6. ]])

c = np.array( [ [1,2], [3,4] ], dtype=complex )
print (c)
#array([[ 1.+0.j,  2.+0.j],
#       [ 3.+0.j,  4.+0.j]])

print (np.zeros( (3,4) ))
#array([[ 0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.],
 #      [ 0.,  0.,  0.,  0.]])
print (np.ones( (2,3,4), dtype=np.int16 ))           # dtype can also be specified

#array([[[ 1, 1, 1, 1],
#        [ 1, 1, 1, 1],
#        [ 1, 1, 1, 1]],
#       [[ 1, 1, 1, 1],
#        [ 1, 1, 1, 1],
#        [ 1, 1, 1, 1]]], dtype=int16)
print (np.empty( (2,3) ) )                                 # uninitialized, output may vary
#array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
#       [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])
os.system("pause")

