# def is_valid_input(letter_guessed):
#     if len(letter_guessed) == 1 and letter_guessed.isalpha() == True:
#         return True
#     else:
#         return False

#
# print(is_valid_input('a'))
# def extend_list_x(list_x, list_y):
#     for n in range(len(list_y)):
#         list_x.insert(n,list_y[n])
#     return print( list_x)
# extend_list_x(['list', 'string', 'int'],[1, 2, 3])


# def extend_list_x(list_x, list_y):
#     """Gets two lists, appends the second one at the beginning of the first one.
#     :param list_x: first list
#     :param list_y: second list
#     :type list_x: list
#     :type list_y: list
#     :return: the appended list: [list_y list_x]
#     :rtype: list
# 	"""
#
#     list_x[:0] = list_y
#     return list_x
# print(extend_list_x(['list', 'string', 'int'],[1, 2, 3]))
def check_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha() == True and letter_guessed.lower() not  in old_letters_guessed
old_letters_guessed = ['a','b']
old_letters = ['a', 'p', 'c', 'f']
letter_guessed ='d'

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True
    else:
        print("X\n", ' -> '.join(sorted(old_letters_guessed)))
        return False


print(try_update_letter_guessed('a',old_letters))