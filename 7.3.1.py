def show_hidden_word(secret_word, old_letters_guessed,):
    new_letters = ''
    for letters in secret_word:
        if letters in old_letters_guessed:
            new_letters += letters + ' '
        else:
            new_letters += "_ "

    return new_letters [:-1]
print(show_hidden_word('typewriter',['t','y']))


# def check_win(secret_word, old_letters_guessed):
#     b = 0
#     for i in secret_word:
#         if i in old_letters_guessed:
#             b += 1
#     return b == len(secret_word)
# print(check_win('',['q']))