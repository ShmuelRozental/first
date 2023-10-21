# arry = [1,33,3,4,0,22,33,44,55]
# def perfect_array(arri):
#     b =0
#     a = len(arri)
#     for nom in arri:
#         b += 1
#
#         if b >= a//2 and 0 < nom < 10:
#             a = True
#
#         elif b <= a//2 and 0 > nom > 9:
#             a =True
#     return a
#
#
#
#
#
#
#
# print(perfect_array(arry))
arry = [9,0,10]


def perfect_array(arri):
    b = 0
    a = len(arri)
    zero = a//2
    for nom in arri:
        if arri[zero] != 0:
            return False
        if b < (a // 2) and  nom > 9 or nom< 0:
            return False
        elif b > (a / 2) and  0 < nom < 9:
            print(nom)
            return False
        b += 1

    return True
print(perfect_array(arry))
