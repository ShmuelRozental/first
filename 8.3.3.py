def count_chars(my_str):
    new_str = my_str.replace(' ','')
    d = 0
    counter = 0
    dict = {}
    for i in new_str:
        for letter in new_str:
            if i == letter:
                counter +=1
        dict[i] = d+counter
        counter = 0


    return dict
print(count_chars("abra cadabra"))