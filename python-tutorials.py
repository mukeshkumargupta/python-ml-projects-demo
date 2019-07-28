import os  #for pause the script

##How to install python and pip
## Rference: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation
##I kept pip file in path:
##F:\Project\external-lib\pip
##How to check pip version : https://stackoverflow.com/questions/40868345/checking-whether-the-pip-is-installed
##Command to install any packacge using pip from command terminal
##But see how to check pip vrsion by seing above link
#python -m pip numpy
##Explore more about https://pypi.org/project/mirpyidl/
##Little info: A library to call IDL (Interactive Data Language) from python

#####################################################################################
#Lists are mutable
# Declaring a list 
L = [1, "a" , "string" , 1+2] 
print L 
L.append(6) 
print L 
L.pop() 
print L
#Output
#[1, 'a', 'string', 3]
#[1, 'a', 'string', 3, 6]
#[1, 'a', 'string', 3]

#tuple is a sequence of immutable
tup = (1, "a", "string", 1+2) 
print tup 
print tup[1] 
#Output
#(1, 'a', 'string', 3)
#a

s = "Hello World"
for i in s : 
    print i 

#Output ach character in nw line

L = [1, 4, 5, 7, 8, 9] 
for  i in L: 
    print i, 
	
#output
#1 4 5 7 8 9

for  i in range(0, 10): 
    print i,
#output	
#output	0 1 2 3 4 5 6 7 8 9
#####################################################################################

##eference: https://stackoverflow.com/questions/11552320/correct-way-to-pause-python-program
##Make delay for some time
#import time
#print("something")
#time.sleep(5.5)    # pause 5.5 seconds
#print("something")

#####################################################################################
print ('\n')
##Function definition
##Reference: https://www.techbeamers.com/understand-python-comment-docstring/
# Define a list of months
print "Function use"
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']

# Function to print the calender months
def showCalender(months):
    # For loop that traverses the list and prints the name of each month
    for month in months:
        print(month)

showCalender(months)

##In triple quotes u can write many numbr of line : Rference: https://www.techbeamers.com/understand-python-comment-docstring/
##Note: Multiline comments don't actually exist in Python
def theFunction():
    '''
This function demonstrate the use of docstring in Python.
This function demonstrate the use of docstring in Python1.
    '''
    print("Python docstrings are not comments.")

print("\nJust printing the docstring value...")
##print(theFunction.__doc__)    ## uncomments when it is required
#####################################################################################

#####################################################################################
##Modular programming in python
##Reference: https://www.python-course.eu/modules_and_modular_programming.php
## A lot of example is given here so u hav to see all the example
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

	
##Note: We can import this module in the interactive python shell and call the functions by prefixing them with "fibonacci.":
print(fib(30))
#Output: 832040
print(ifib(100))
ifibAlias = ifib
print(ifibAlias(100))
#Output: 354224848179261915075L
#####################################################################################

#####################################################################################
## A lot of basic article given on python and numpy
#Rference: http://cs231n.github.io/python-numpy-tutorial/

#####################################################################################

os.system("pause")