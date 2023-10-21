list_by = input('add a list').split(',')
a = []
while True:
    i = int(input("add num"))

    if i == 1:
        print(list_by)
    elif i == 2:
         print(len(list_by))
    elif i == 3:
        check = input("please enter a product name")
        print(check in list_by)
    elif i == 4:
        product = input("enter a name product")
        print(list_by.count(product))
    elif i == 5:
        list_by.remove(input("remove an item: "))
    elif i == 6:
        list_by.append(input("enter a name product"))
    elif i == 7:
        print([short for short in list_by if len(short) < 3 or not short.isalpha()])
    elif i == 8:
        list_by = list(set(list_by))
    elif i == 9:
        break  # Exit the loop if the user enters '9'


