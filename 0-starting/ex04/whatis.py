import sys

def check_odd_or_even(number: int):

    if not isinstance(number, int):
        raise ValueError()
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    arg_len = len(sys.argv)
    if arg_len > 2:
        raise AssertionError("more than one argument is provided")
    elif arg_len == 2:
        number = int(sys.argv[1])
        check_odd_or_even(number)

except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print(f"AssertionError: argument is not an integer")