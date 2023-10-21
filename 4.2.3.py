# a = input("add").lower()
# b = float(a[:-1])
# if a[-1] == "f":
#    print((5 * b -160)/9)
# if a[-1] == "c":
#     print((9 * b + 32*5)/5)
a = input("aaaa")
if len(a)>1 and a.isalpha() == False:
    print("E3")
elif len(a)>1:
    print("E1")
elif a.isalpha() == False:
    print("E2")
else:
    print(a.lower())