def distance(num1, num2, num3):
    if ((num1 - num3) == 1 or abs(num1- num2) == 1) and (abs(num1 - num2) >= 3 or (num1 - num3) >= 3):
        return True
    else:
        return False


print(distance(0,1,10))
