"""
Write a program that takes a bill_amt and number_of_people_to_split_the_bill and then prints the user back with 18% tax added on bill and also prints how many each one should pay the amount after split

* Use functions 

Hint✨: make sure you typeCast user input before performing any math operations

INPUT:
  'Enter the bill amount $'250
  'No of people to split the bill.' 2
OUTPUT:
  Total amount = 287.5
  Each one should pay = 143.75

  # eg 
# Input amount =1000 people = 4  
# Output 1180 /4 = 295 
"""
# S1: input_bill_amount(int) bill amount and no_of_people(int)
input_bill_amount =int(1000)
no_of_people=int(4)
# S2: Add 18% tax on input_bill_amount as total_amount
total_amount=input_bill_amount+(input_bill_amount*18/100)

# S3: split_bill= total_amount/no_of_people
split_bill=total_amount/no_of_people 

# Sn: split_bill = Amount for each person after split 
print("Amount to be paid by each person :",end="")
print(split_bill)