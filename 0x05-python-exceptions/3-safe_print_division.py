#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        calc = a / b
    except (ZeroDivisionError, TypeError):
        calc = None
    finally:
        print("Inside result: {}".format(calc))
    return calc
