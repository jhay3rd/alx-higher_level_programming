#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for j in my_list:
        if j > max_num:
            max_num = j
    return max_num
