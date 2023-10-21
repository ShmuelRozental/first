def mult_tuple(tuple1, tuple2):
    new_tup = ()
    for i in tuple1:
        for y in tuple2:
            oob = ((i,y),(y,i))
            new_tup += oob
    return new_tup
first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))