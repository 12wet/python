class SingleList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        
    def insert_head(self, node):
        if self.head:
            node.nextNode = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.nextNode = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.head = self.head.nextNode
        node.nextNode = None
        self.length -= 1
        return node

    def remove_tail(self):   # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.head is None:
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            current = self.head
            while current.nextNode != self.tail:
                current = current.nextNode
            current.nextNode = None
            self.tail = current
        self.length -= 1
        return node   # zwracamy usuwany node

    def join(self, other):   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        elif not other.head is None:
            self.tail.nextNode = other.head
            self.tail = other.tail
            self.length += other.length
        other.clear()

    def clear(self):   # czyszczenie listy
        while not self.head is None:
            self.remove_head()
