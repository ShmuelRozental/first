def last_early(my_str):
    str = my_str.lower()
    return str[-1] in str[:-1]
print(last_early("ssdddd"))