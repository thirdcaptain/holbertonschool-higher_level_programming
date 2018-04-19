#!/usr/bin/python3
#def uniq_add(my_list=[]):
#    sum = 0
#    for element in my_list:
#        count = my_list.count(element)
#        if count > 1:
#            for i in range(count - 1):
#                my_list.remove(element)
#    for element in my_list:
#        sum += element
#    return sum
def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum = 0
    print (set_list)
    for element in set_list:
        sum += element
    return sum
