# 3. Functions with return statements

def finance(amt):
    global final
    interest = 100
    final = amt +interest
    return final
    

#finance(1000) - 1100 = finance(1000)
#b=finance(1000)  -  b will have returned  value - 1100 = b = finance(1000)
finance(1000)
# 1100
print(finance(1000))
b=finance(1100)
print(b)
finance(1500)  # 1600  
print("Global variable")
print(final)
print("Global variable assigned to local")
locvar=final
print(locvar)






