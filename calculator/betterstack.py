class Stack:
    def __init__(self, size=0):
        self.size = size
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return -1
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0


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


def ReversePolishNotationConvertor(mstring):
    rise = 0
    lastpriority = 0
    littlestack = Stack(0)
    result = ""

    for x in mstring:

        if x.isnumeric():
            result += x
        else:
            if x == '(':
                rise += 2
            elif x == ')':
                rise -= 2
            else:
                result += " "
                if lastpriority <= priority[x] + rise:
                    littlestack.push(x)
                    littlestack.push(" ")
                    lastpriority = priority[x] + rise
                else:
                    while not littlestack.is_empty():
                        result += littlestack.pop()
                    littlestack.push(x)
                    littlestack.push(" ")
    while not littlestack.is_empty():
        result += littlestack.pop()
    return result


def ReversePolishNotationCalculator(rpn_string):
    expression = rpn_string.split()
    stack = Stack(0)
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




