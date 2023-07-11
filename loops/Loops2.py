# While
    # While loop is used when we are not specific about outcome, when to get out of loop

# no = 1
# while no < 10:
#     print(no)
#     no += 1


# break 
# continue

# Program that take coins of 1, 2, 5 else will be asking them again and again
isCoin = True
while isCoin:
    userInput = input("ENter a coin")
    if userInput in ["1", "2", "5"]:
        print("Accepted coin")
        isCoin = False

