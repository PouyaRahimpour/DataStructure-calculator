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

