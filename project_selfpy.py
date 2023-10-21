def check_win(secret_word, old_letters_guessed):
    counter = 0
    for i in secret_word:
        if i in old_letters_guessed:
            counter += 1
    return counter == len(secret_word)


def show_hidden_word(secret_word, old_letters_guessed,):
    new_letters = ''
    for letters in secret_word:
        if letters in old_letters_guessed:
            new_letters += letters + ' '
        else:
            new_letters += "_ "

    return new_letters [:-1]


def check_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and\
        letter_guessed.isalpha() == True and\
        letter_guessed.lower() not  in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True
    else:
        print("X\n", ' -> '.join(sorted(old_letters_guessed)))
        return False

try_update_letter_guessed('x',['a','u','s'])