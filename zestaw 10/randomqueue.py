import random

class RandomQueue:

    def __init__(self, size=10):   # wersja z ograniczeniem na rozmiar
        self.size = size
        self.queue = []

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise ValueError()
        self.queue.append(item)

    def remove(self):   # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise ValueError()
        index = random.randint(0, len(self.queue) - 1)
        self.queue[index], self.queue[-1] = self.queue[-1], self.queue[index]
        return self.queue.pop()

    def is_empty(self):
         return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def clear(self):   # czyszczenie listy
        self.queue = []