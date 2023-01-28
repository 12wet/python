class Node:

    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def __str__(self):
        return str(self.value)