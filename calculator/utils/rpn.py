from .stack import Stack

priority = {
    -1: -1,
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '^': 2,
    '(': 2,
    ')': 2
}


def reverse_polish_notation_convertor(math_string):
    rise = 0
    last_priority = 0
    stack = Stack()
    result = ""

    for x in math_string:

        if x.isnumeric():
            result += x
        else:
            if x == '(':
                rise += 2
            elif x == ')':
                rise -= 2
            else:
                result += " "
                new_priority = priority[x] + rise
                if last_priority <= new_priority:
                    stack.push(x)
                    last_priority = new_priority
                else:
                    while not stack.is_empty():
                        result += stack.pop() + " "
                    stack.push(x)
    result += " "
    while not stack.is_empty():
        result += stack.pop() + " "
        
    return result


def reverse_polish_notation_calculator(rpn_string):
    expression = rpn_string.split()
    stack = Stack()
    for element in expression:
        if element == "+":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(str(y + x))
        elif element == "-":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(str(y - x))
        elif element == "*":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(str(y * x))
        elif element == "/":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(str(y // x))
        elif element == "^":
            x = int(stack.pop())
            y = int(stack.pop())
            stack.push(str(y ** x))
        else:
            stack.push(element)
    answer = stack.pop()
    return answer



