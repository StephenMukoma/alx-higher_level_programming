#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    list_result = list()
    for i in my_list:
        if i % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result
