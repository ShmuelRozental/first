import numbers


def numbers_letters_count(my_str):
    a = 0
    b = 0
    lista = []

    for i in my_str:
        if i.isdigit():
            a += 1
        else:
            b += 1
    lista.append(a)
    lista.append(b)
    return lista


print(numbers_letters_count('abc!@# 6.3'))

