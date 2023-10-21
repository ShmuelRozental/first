def longest (my_list):
    sorted_list = sorted(my_list, key=len)
    return sorted_list[-1]

