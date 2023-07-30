# Variable Function

# math program takes two input parameters
# Parameter1: [1,3 ], Parameter2 Operater +-*%/

print("Example for Variable Function/Parameter")

def math(number, name):

    result = number[0] + number[1]
    print(f"Result: {result}, Name: {name}")


name="Muzamil"
number=[1,4]
# math(number=n1, name=na)
math(name=name, number=number)