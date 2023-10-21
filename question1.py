
# while True:
#     num = input("enter your num")
#     print(num)

# num = ("")
# while num != "666":
#     num = input('enter your number')
#     print(num)
i = 0
num = ("")
while num != "666":
    num = input('enter your number')
    if len(num) != 3:
        print("please enter 3 num")
    elif num[0] != num[1] and num[1] != num[2] and num[2] != num[0]:
           print(num)
           i += 1
           print(i)


