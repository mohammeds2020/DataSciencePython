# Arbitrary Arguments. (*args)

"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""


def myfunc(name, age, *income_streams): # *income_stream is an optional arg and it returns a tupple
    print(f"name is {name}, {income_streams[0]}")
    print(type(income_streams))

myfunc('Muzamil', 36, 'Engineer', "business", "Teacher")
# after function is being called the above data
# income_streams = ('Engineer', "business", "Teacher")


## eg:

def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)