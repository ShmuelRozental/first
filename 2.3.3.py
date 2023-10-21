num = int(input("Enter three digits (each digit for one pig):"))
a = num//100
ab = num % 100
b = ab // 10
c =ab % 10
sum = a+b+c
print(sum,sum//3,sum%3,sum % 3 == 0)