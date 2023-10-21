dict_name = {"first_name" : "maria","last_name":"carey", "birth_date":"27.03.1970","hobbies":["Sing", "Compose", "Act"]}
num_inpt = int(input("enter number 1-7"))
if num_inpt == 1:
    print(dict_name["last_name"])
if num_inpt == 2:
    print(dict_name["birth_date"])
if num_inpt == 3:
    print(len(dict_name["hobbies"]))
if num_inpt == 4:
    print(dict_name["hobbies"])
if num_inpt == 5:
    dict_name["hobbies"].append("Cooking")
if num_inpt == 6:
    dict_name["birth_date"]= (27,3,1970)
    print(dict_name["birth_date"])
if num_inpt == 7:
    dict_name ["age"] = 52
    print(dict_name["age"])
