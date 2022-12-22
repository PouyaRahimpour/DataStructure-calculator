class Stack:
    def __init__(self, size):
        self.elements = []
        self.size = 0

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
    littlestack = Stack(0)
    littlelist = []
    x = 0
    while x < len(mstring):

        if mstring[x].isnumeric():
            littlelist.append(mstring[x])
            x += 1
        else:
            if mstring[x] == '(':
                priority["+"] += priority["("]
                priority["-"] += priority["("]
                priority["/"] += priority["("]
                priority["*"] += priority["("]
                priority["^"] += priority["("]
                x += 1
            elif mstring[x] == ')':
                priority["+"] -= priority[")"]
                priority["-"] -= priority[")"]
                priority["/"] -= priority[")"]
                priority["*"] -= priority[")"]
                priority["^"] -= priority[")"]
                x += 1
            else:
                if priority[littlestack.peek()] <= priority[mstring[x]]:
                    littlestack.push(mstring[x])
                    x += 1
                else:
                    while not littlestack.is_empty():
                        littlelist.append(littlestack.pop())
                    littlestack.push(mstring[x])
                    x += 1
    return littlelist
