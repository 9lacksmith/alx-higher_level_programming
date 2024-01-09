#!/usr/bin/python3

def no_c(my_string):
    if "c" in my_string:
        my_string = my_string.translate({ord('c'): None})
        return my_string.translate({ord('C'): None})
    elif "C" in my_string:
        my_string = my_string.translate({ord('C'): None})
        return my_string.translate({ord('c'): None})
    else:
        return my_string
