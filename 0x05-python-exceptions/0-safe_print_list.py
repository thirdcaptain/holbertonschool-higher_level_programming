#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except:
            print()
            return count
    print()
    return count

#    count = 0
#    sum = 0
#    try:
#        for element in range(x):
#            print("{}".format(my_list[element]), end="")
#            count += 1
#    except:
#        pass
#    finally:
#        print()
#        return count
