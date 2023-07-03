# Conditions

student_attendence = 85
if (student_attendence > 75):
    print("Yes you're eligible for test")

# exceptions
# < 75
# = 75

# Else 
if student_attendence > 75:
    #if True it will execute the code under indentations
    print("Yes you're eligible for test")
else:
    print("You cant attend the exam")

# Elseif (elif)

if student_attendence > 75:
    #if True it will execute the code under indentations
    print("Yes you're eligible for test")
elif student_attendence == 75:
    print("You just saved this time")
elif student_attendence>65 and  student_attendence<75:
    print("attendence morethan 65 but lessthan eligible ")
else:
    print("You cant attend the exam")

#