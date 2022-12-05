#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = list()
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range (0, len(my_list) - 1):
            if i == 3:
                pass
            new_list.append(my_list[i])
    return new_list
