#  Function

# math program takes two input parameters
# Parameter1: [1,3 ], Parameter2 Operater +-*%/


print("Example for Keyword Function/Parameter")
def math(number, name):
    # result = 1 + 3
    result = number[0] + number[1]
    # print("Result: ")
    # print(result)
    # print("Name: ", name)

    # print("Formated strings")
    #Formated Strings / Short Hand syntax
    print(f"Result: {result}, Name: {name}")

math(name="Muzamil", number=[1,4])