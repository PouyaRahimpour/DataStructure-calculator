from .rpn import *

def evaluate_math_string(math_string):
    rpn_string = reverse_polish_notation_convertor(math_string)
    result = reverse_polish_notation_calculator(rpn_string)
    return result