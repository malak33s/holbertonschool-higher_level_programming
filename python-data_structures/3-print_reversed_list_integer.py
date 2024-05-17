def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    num = length - 1
    while num >= 0:
        number = my_list[num]
        print("{:d}".format(number))
        num = num - 1
