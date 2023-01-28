class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.currSize = 0
        self.size = size

    def is_empty(self):
        return self.currSize == 0

    def is_full(self):
        return self.size == self.currSize

    def push(self, data):
        if self.is_full():
            raise ValueError()
        self.items[self.currSize] = data
        self.currSize += 1

    def pop(self):
        if self.currSize == 0:
            raise ValueError()
        self.currSize -= 1
        data = self.items[self.currSize]
        self.items[self.currSize] = None
        return data