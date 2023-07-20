"""
Write a program to convert camelCase to snake_case

input: myFunction
output: my_function

Hint✨: use string manipulation method .isupper() and a for loop
myFun
"""
#S1: input: myFunction
#S2: find capital char

    # F -> _F -> _f
    #S3: replace upper char to lower char
    #S4: prefixing(concatinating) underscore '_' with above lower char
#Sn: output: my_function


#S1: input: myFunction
user_input = "myFunctionHere"
user_input = "myFunctionHere &Name,"
final_output = []
 
#S2: find capital char
for char in user_input:
    if char.isupper():# F
        print(char)
        #S3: replace upper char to lower char
        uppered = char.lower()
        print(uppered)

        #S4: prefixing(concatinating) underscore '_' with above lower char
        a1 = "_" + uppered
        print(a1)

        #S5: concatinating lower with _lower chars
        final_output.append(a1)

    else:
        final_output.append(char)

#Sn: output: my_function
print(final_output)
for char in final_output:
    # print(char, end="\n")
    print(char, end="")


# def snake_case(user_input):
#     for char in user_input:

#         #myFunctionHere
#         if char.isupper():
#             print(i.lower())
#             j=i     


# # user_input= input("Enter string in camelcase : \n ")
# user_input = "myFunctionHere"
# snake_case(user_input)