def get_only_price (s):
    return s[-1]
def sort_prices(list_of_tuples):
    list_of_tuples= sorted(list_of_tuples,key= get_only_price)
    list_of_tuples.reverse()
    return list_of_tuples
print(sort_prices([('milk', '5.'), ('candy', '2.5'), ('bread', '9.0')]))
