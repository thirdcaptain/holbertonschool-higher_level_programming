#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for element in my_list:
        print(my_list)
        print(element)
        count = my_list.count(element)
        if count > 1:
            for i in range(count - 1):
                print(my_list)
                my_list.remove(element)
    print(my_list)
    for element in my_list:
        sum += element
    return sum
