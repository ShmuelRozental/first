def chocolate_maker(small, big, x):
    small = 1 * small
    big = 5 * big
    if big + small >= x:
        return True
    else:
        return False
print(chocolate_maker(5,5,17))