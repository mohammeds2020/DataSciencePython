# Strings

# Assigning string to a varible
b="hello"
print(b)

# Multiline String
a = """Hi there sadf
this
"""

# Strings as Arrays
# l = [0, "a"] example
# print(l[1])

a = "hello"
print(a[-2])


#Looping through a string
for i in a:
 print(i)

# exercise:

peoples = ['m', 'f', 'f', 'm', 'f']

for people in peoples:
    if people == "m":
        print("Yes male")
    else:
        print("NO- female")

a = "goodbye"
for i in a:
   print(i)

# length
print(len(a))

# in operator
a = "My name is faizan"
print("nam " in a) # return bool value

# not operator, shorthand syntax
print("nam " not in a)
