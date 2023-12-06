#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    density = 0
    for score, weight in my_list:
        number += score * weight
        density += weight
    weight_average = number / density
    if density == 0:
        return 0
    return weight_average
