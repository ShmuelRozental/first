#
#
# def seven_boom(end_number):
#     a = []
#     n = 0
#     while n <= end_number:
#         if n % 7 == 0 or n % 10 == 7:
#             a.append("BOOM")
#             n += 1
#         else:
#             a.append(n)
#             n += 1
#     return a
# print(seven_boom(17))

def sequence_del(my_str):
    if not my_str:
        return my_str
    new_str = my_str[0]
    for i in range(1,len(my_str)):
        print(i)
        if my_str[i] != my_str[i-1]:
            new_str += my_str[i]

    return new_str

print(sequence_del(""))
