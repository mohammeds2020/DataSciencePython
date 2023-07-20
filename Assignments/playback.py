import pdb
'''

input =This is CS50.                                                                   
output = This...is...CS50.  


'''
# step 1 accept input  =This is CS50. 
input="This is CS50."
output=""
# step 2 whenever we encounter space convert it in ...
# for space in input:
#     if space==' ':
#     if ' ' in input:

#         output= "..." + output 

#         print(output,end="")
#     else:
#         output=space
#         print(output,end="")

output = input.replace(" ", "...")
print("New"+output)


#break and continue useage

# Step n output should be  This...is...CS50.


# tick the path