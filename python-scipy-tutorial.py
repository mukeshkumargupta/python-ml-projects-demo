##Very good reference for tutorial

##refrence Very good tutorial first practic fron : https://www.geeksforgeeks.org/python-introduction-matplotlib/
##For more in details: https://docs.scipy.org/doc/scipy/reference/tutorial/

#####################################################################################
import os
from scipy import special   #same for other modules
import numpy as np
from scipy import io as sio
#####################################################################################
from scipy.special import cbrt
#Find cubic root of 27 & 64 using cbrt() function
cb = cbrt([27, 64])
#print value of cb
print(cb)
#####################################################################################

#####################################################################################
from scipy.special import comb
#find combinations of 5, 2 values using comb(N, k)
com = comb(5, 2, exact = False, repetition=True)  ##if rep true then 15 otherwise 10
print(com)
#####################################################################################

#####################################################################################
from scipy.special import perm
#find permutation of 5, 2 using perm (N, k) function
per = perm(5, 2, exact = True)
print(per)
#####################################################################################

os.system("pause")

