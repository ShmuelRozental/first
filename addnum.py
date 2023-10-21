def add_numbers(num):
    tutal = 0
    while num > 0:
         degit = num % 10
         tutal += degit
         num //= 6
    return tutal


input_num = int(input("enter anumber: "))
result = add_numbers(input_num)
print(result)




