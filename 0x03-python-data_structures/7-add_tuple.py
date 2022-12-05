#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    tup_1 = list(tuple_a)
    tup_2 = list(tuple_b)
    if len(tup_1) < 2:
        if len(tup_1) == 1:
            tup_1.append(0)
        else:
             tup_1.append(0)
             tup_1.append(0)
    if len(tup_2) < 2:
        if len(tup_2) == 1:
            tup_2.append(0)
        else:
            tup_2.append(0)
            tup_2.append(0)
    return (tup_1[0] + tup_2[0]), (tup_1[1] + tup_2[1])
