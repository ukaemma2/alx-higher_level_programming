#!/usr/bin/python3

def safe_print_division(a, b):
    result = a/b
    try:
        result = result
        except ZeroDivisionError:
            result = None
        except TypeError:
            result = None
        finally:
            print('Inside result{}'.format(result))
            return result
