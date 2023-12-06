#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set()
    sum_uniq = 0
    for j in my_list:
        if j not in uniq_list:
            uniq_list.add(j)
            sum_uniq += j
    return sum_uniq
