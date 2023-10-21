def squared_numbers(start,stop):
    result =[]
    while start <= stop:
        result.append(start**2)
        start += 1
    return result

print(squared_numbers(2,33))