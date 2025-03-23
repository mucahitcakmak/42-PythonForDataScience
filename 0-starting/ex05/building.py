import sys

def text_lover(text: str):
    """Returns the count of each of the contents of the given text

    Args:
        text (str): any sentence
    """
    total_ch = len(text)
    upper_count = sum(1 for ch in text if ch.isupper())
    lower_count = sum(1 for ch in text if ch.islower())
    punctuation_ch = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_count = sum(1 for ch in text if ch in punctuation_ch)
    space_count = sum(1 for ch in text if ch.isspace())
    digit_count = sum(1 for ch in text if ch.isdigit()) 

    print(f"The text contains {total_ch} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2:
            text = input("What is the text to count?\n")
            text += "\n"
            text_lover(text)
        else:
            text_lover(sys.argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        pass

if __name__ == "__main__":
    main()