def add_digits (num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

num_input = 0
input_sum = 0
counter = 0
total = 0

while num_input != 500:
    input_sum += add_digits(num_input)
    num_input = int(input("enter a number; "))
    counter += 1
    if num_input % 2 != 0:
        print(add_numbers(num_input))
else:
    print(input_sum / counter)
    print(input_sum)



