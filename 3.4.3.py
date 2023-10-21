mystr = input("please enter sum string")
lengthstr = len(mystr)
half = (lengthstr // 2)
#print(x)
first_str = mystr.lower()[:half]
last_str = mystr.upper()[half:]

print(first_str + last_str)