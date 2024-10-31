from .rpn import *

def evaluate_math_string(math_string):
    print("expression is: ", math_string)
    rpn_string = reverse_polish_notation_convertor(math_string)
    print("rpn is: ", rpn_string)
    result = reverse_polish_notation_calculator(rpn_string)
    print("result is: ", result)
    return result