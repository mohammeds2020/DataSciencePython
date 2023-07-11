# For Loop

#break

peoples = ["p1", "p2", "p3", "p4"]

for p in peoples:
    print(p)
    if p == 'p3':
        break

# continue
for p in peoples:
    if p == 'p3':
        continue
    print(p)

# Behaviour of continue and break keyword
for p in peoples:
    if p == 'p3':
        continue
        #From here code will not be execeted
        print(p)
        

# Range
# a = 0
# for i in peoples:
#     print(a)
#     a += 1

for i in range(5):
    print(i)

print("range parameters")
for i in range(2, 10, 2):
    print(i)

# Nested loops
name = "muzamil"
result = ''
for char in name:
    print(char)
    if char in ['a', 'e', 'i', 'o', 'u']:
        result += char.upper()
        print(result)

    else:
        result += char
        print(result)

print(result)

# Nested loop eg2
fruits = ["apples", "banana", "grapes"]
colors = ["green", "red", "black"]

for fruit in fruits:
    for color in colors:
        print(fruit, color)


# Nested loop eg2
fruits = [["apples", "banana", "grapes"],["green", "red", "black"]]
print("\nNested loop ex2")
for fruit in fruits:
    for f in fruit:
        print(f, end="-")

# Nested loop eg 3
fruits = [["apples", "banana", "grapes"],["green", "red", "black"]]
print("\nNested loop ex3")

for fruit in fruits:
    print(type(fruit))
    print(fruit) # 1st iteration, fruit =["apples", "banana", "grapes"] / This is index of fruits[0]
                 # 2nd iteration, fruit =["green", "red", "black"] / This is index of fruits[1]

    for f in fruit: 
        print(f, end="-")
