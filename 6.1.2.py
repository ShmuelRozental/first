def shift_left (my_list):
    first_list = my_list[0]
    last_list = my_list[1:]
    last_list.append(first_list)
    return last_list
print(shift_left([1,2,3]))
