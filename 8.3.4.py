course_dict = {'I': 3, 'love': 3, 'self.py!': 2, 'ddddd':5,  'cccc':5}
def inverse_dict(my_dict):
    new_dict ={}
    for key in my_dict.keys():
        a = []
        if my_dict[key] in new_dict:
            new_dict[my_dict[key]].append(key)
            new_dict[my_dict[key]].sort()


        else:
            a.append(key)
            new_dict[my_dict[key]] = a
    return new_dict

print(inverse_dict(course_dict))
#
#
# course_dict = {'I': 3, 'love': 3, 'self.py!': 2, 'ddddd': 5, 'cccc': 5}
#
#
# def inverse_dict(my_dict):
#     new_dict = {}
#
#     for key, value in my_dict.items():
#         if value in new_dict:
#             new_dict[value].append(key)
#             new_dict[value].sort()
#         else:
#             new_dict[value] = [key]
#
#     return new_dict
#
#
# print(inverse_dict(course_dict))
