##Very good reference for tutorial

##refrence Very good tutorial first practic fron : https://www.geeksforgeeks.org/python-introduction-matplotlib/

#####################################################################################
import os
# importing matplotlib module  
from matplotlib import pyplot as plt 
import matplotlib.image as mpimg  ## Other way to import
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot 
plt.plot(x,y) 
  
# function to show the plot 
#plt.show()
#####################################################################################

#####################################################################################
# importing matplotlib module  
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot the bar 
plt.bar(x,y) 
  
# function to show the plot 
#plt.show() 
#####################################################################################


#####################################################################################
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot histogram 
plt.hist(y) 
  
# Function to show the plot 
#plt.show() 
#####################################################################################


#####################################################################################
##Rference: to draw images https://matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py
##Not working need to see why
#img = mpimg.imread('images/stinkbug.png')
#print(img)

#####################################################################################

#####################################################################################
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot scatter 
plt.scatter(x, y) 
  
# function to show the plot 
plt.show() 
#####################################################################################


os.system("pause")

