#Placement operation for input number
# and The sum of all input operations
#and The number of iterations
num_input = 0
input_sum = 0
average = 0
#A loop to create a new input if a number less than five hundred is entered
while num_input !500:
    num_input = int(input("enter number"))
    average += 1
    input_sum += num_input
    if num_input % 2 != 0 and num_input != 500:
        hundert_digit = num_input // 100
        last_digit = num_input % 100
        num_2 = last_digit//10
        num_3 = last_digit % 10

        # Calculate the sum of digits
        digit_sum = hundert_digit+num_2+num_3

        print(digit_sum)
        print("your average is: ", input_sum / average)
else:
    print ("500 is max")

