import sys

def main():
    """The given argument is converted to Morse Code"""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
        "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. "
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        
        converted = ""
        for ch in sys.argv[1].upper():
            if ch not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            converted += NESTED_MORSE[ch]
            
        print(converted.rstrip())
    
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()