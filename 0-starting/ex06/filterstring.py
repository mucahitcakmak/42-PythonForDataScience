import sys
import ft_filter

def main():
    """Accepts only 2 arguments:
        1. string
        2. integer

    Returns a list of words that are longer than the integer
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        
        text = sys.argv[1]

        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        
        checker = lambda item: len(item) > num
        result = list(ft_filter.ft_filter(checker, text.split()))
        
        print(result)
    except ValueError as e:
        raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()