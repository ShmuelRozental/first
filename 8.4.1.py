HANGMAN_PHOTOS = {"picture 1" :
    "x-------x"

,"picture 2":
"""    x-------x
    |
    |
    |
    |
    |
"""
,"picture 3":
"""    x-------x
    |       |
    |       0
    |
    |
    |
"""
,"picture 4":
"""    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
,"picture 5":
"""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""
,"picture 6":
"""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""
,"picture 7":
"""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""    }
a = HANGMAN_PHOTOS.keys()


def print_hangman(num_of_tries):
    picture_key = "picture {}".format(num_of_tries)
    if picture_key in HANGMAN_PHOTOS:
        print(HANGMAN_PHOTOS[picture_key])
    else:
        print("תמונה לא נמצאה")

print_hangman(4)