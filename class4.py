#import the required lib
# import random
from random import randrange
#call  friend

#Function
# block the code that is ment to do something and it executes

"""
- reuseable
- return
"""


#GLobal variable
# n = "Faizan"
# def greet(name):
#     global name1
#     name1 = "Muzamil"
#     print("hello" + name + name1)

# # WE are tring to access a varible which is not defined
# print(name1)
# #calling the function
# greet("Name")


#2nd way
name1 = ''
def greet(name):
    name1 = "Muzamil"
    print("hello" + name + name1)

greet("Faizan")
print(name1)


#DATA TYPES
# Most used datatypes

"""
- str
- int 
- dict
- list
- set
- bool
"""

x = 'str'
x = 1
x = (1,2,3) #tuple #immutable
x = [1,2,3] #list #mutable 
x = {"name":"faizan"} #dict
x = {1, "string"} #set
x = True #boolean
x = None

# Type casting
x = str(1)
x = int(1)

#Convert int to float
x = 23

y = float(x)
print(type(y))

r = random.randrange(1, 10)
print(r)

#Modules
#1. import a whole module
import random
#using this model
random.randrange()


# 2. Import specific function of module
from random import randrange
#useage
randrange()

