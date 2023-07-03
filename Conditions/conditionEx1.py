# Program that calculute the maths opertations

# GIGO -> Garbage in  Garbage out

# INput: 1 + 2
# ouput: 3
# * - /

# "1 + 2"
user_input = input("enter number \n").split(" ")
# print(type(user_input[0]))

x = int(user_input[0])
operator = user_input[1]
y = int(user_input[2])
# print(type(y))

if operator == '+':
    print("This is an addition operator")
    result = x+y
elif operator == '-':
    print("This is an subtraction operator")
    result = x-y
    print(result)
elif operator == '*':
    print("This is an multiplaction operator")
    result = x*y
    print(result)
elif operator == '/':
    print("This is an divison operator")
    result = x/y
    print(result)    
else:
    print("This is not an valid  operator") 
    