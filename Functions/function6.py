# Arbitray Keyword (**kargs)
"""
  In the function, we use the double asterisk ** before the parameter name to denote this type of argument. The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.
"""

def myfunc(**data): #*income_stream is an optional and its a dictionary
  # data = {name="hi", age=12, location="BLR"}
  
  #dict_items([('name', 'Ron'), ('age', 12), ('location', 'BLR')])
  for key, value in data.items():
    print(f"{key}, {value}")
  print("", end='\n')


myfunc(name="hi", age=12, location="BLR")
myfunc(name="Goodbye", age=20, location="AUS")