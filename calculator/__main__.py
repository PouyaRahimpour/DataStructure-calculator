from utils.rpn import *
if __name__ == "__main__":
    math_string = "".join(input().split())
    math_string_polished = reverse_polish_notation_convertor(math_string)
    answer = reverse_polish_notation_calculator(math_string_polished)
    print(answer)
    
