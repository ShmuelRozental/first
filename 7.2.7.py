# def arrow(my_char, max_length):
#     num = 0
#     arrow_pattern = ' '
#     for num in range(max_length):
#         num += 1
#         arrow_pattern+= my_char * num
#     for i in range(max_length):
#         max_length -= 1
#         arrow_pattern += my_char*max_length
#     return arrow_pattern
#
# def arrow(my_char, max_length):
#     arrow_pattern = ""
#     for num in range(max_length):
#         num += 1
#         arrow_pattern += my_char * num+'\n'
#
#     for i in range(max_length):
#         max_length -= 1
#         arrow_pattern += my_char * max_length+'\n'
#
#     return arrow_pattern
#
#
#
# arrow('d',3)

def arrow(my_char, max_length):
    arrow_pattern = ""
    for num in range(max_length):
        num += 1
        arrow_pattern += my_char * num + '\n'

    for i in range(max_length):
        max_length -= 1
        arrow_pattern += my_char * max_length + '\n'

    return arrow_pattern.rstrip('\n')

result = arrow('d', 3)
print(result)