# Python convention dictates that errors should not be silenced, sometimes we want to raise an exception ourselves:


def list_average(arg_list):
    if not arg_list:
        raise ValueError("The argument list is empty, average of empty is undefined.")
    return sum(arg_list) / len(arg_list)


my_list = [5, 4, 10, 19]
print(list_average(my_list))
print(list_average([]))
