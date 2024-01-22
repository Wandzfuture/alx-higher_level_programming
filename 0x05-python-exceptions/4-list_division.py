#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                if type(my_list_1[i]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                    print("wrong type")
                else:
                    result[i] = my_list_1[i] / my_list_2[i]
            else:
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
    return (result)
