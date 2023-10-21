ipt = 0
counter =0
sum = 0
lst_num =[]
while counter < 3:
    ipt = int(input("enter num"))
    counter += 1
    sum += ipt
    lst_num.append(ipt)
for num in lst_num:
    if num > sum/counter:
        print(num)

print(sum/counter)
