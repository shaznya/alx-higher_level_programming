#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []

    for num in my_list:
        multiple_of_2 = num % 2 == 0
        list_result.append(multiple_of_2)

    return list_result
