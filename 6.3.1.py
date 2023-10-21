def are_lists_equal (list1,list2):
     sort_list1 = sorted(list1)
     sort_list2 = sorted(list2)
     return sort_list1 == sort_list2
print(are_lists_equal([1,4.5,3],[2,4.5,1]))