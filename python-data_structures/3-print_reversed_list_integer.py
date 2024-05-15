def print_reverse_list(my_list=[]):
    length = len(my_list)
    num = length - 1
    while num >= 0:
        number = my_list[num]
        print(num)
        num = num - 1
