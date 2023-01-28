from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1 + self.pt2).x / 2, (self.pt1 + self.pt2).y / 2)

    def area(self):             # pole powierzchni
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1 += Point(x, y) 
        self.pt2 += Point(x, y) 

    def intersection(self, other): # część wspólna prostokątów
        if (self.pt1.x > other.pt2.x) or (self.pt2.x < other.pt1.x) or (self.pt1.y > other.pt2.y) or (self.pt2.y < other.pt1.y):
            raise ValueError()
        else:
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):    # prostąkąt nakrywający oba
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):           # zwraca krotkę czterech mniejszych
        return (
            Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y),
            Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y),
            Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y),
            Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y))

    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C
