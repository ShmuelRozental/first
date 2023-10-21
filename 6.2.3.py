def format_list(my_list):
    return ', '.join(my_list[:-1:2])+ ", and " + my_list[-1]

print(format_list(["1","2","3","4","5","6"]))
