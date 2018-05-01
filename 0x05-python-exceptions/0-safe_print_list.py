def safe_print_list(my_list=[], x=0):
    count = 0;
    sum = 0;
    try:
        for element in range(x):
            print("{}".format(my_list[element]), end="")
            count += 1
    except:
        for element in range(my_list):
            sum += 1
    finally:
        print()
        return count
