from betterstack import ReversePolishNotationConvertor
ReversePolishNotationConvertor()

if __name__ == __main__:
    math_string = input()
    math_string = "".join(math_string.split())
    print(ReversePolishNotationConvertor(math_string))
