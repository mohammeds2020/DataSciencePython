## Functions without arguments

# They are blocks of code that are executed when ever we call them

a, b = 1, 2
sum = a + b
print(sum)

# different types of functions
# 1. Built-in function
print("Hello")

#creating a function for the about code
# 2. User-defined functions
#  1. Function without args
   
def addition():
    a, b = 1, 2
    sum = a + b
    print(sum)


print("Calling the function")
addition()

# 2. User-defined functions
#    2. Functions with arguments

def math(a):
    sum = a + 1
    print(sum)

user = int(input("Enter a value"))

math(user)
 
 
