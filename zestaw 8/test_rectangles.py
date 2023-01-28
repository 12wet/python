from rectangles import Rectangle, Point


def test_from_points():
    assert str(Rectangle.from_points(
        [Point(1, 2), Point(4, 4)])) == '[(1, 1), (4, 4)]'

    assert Rectangle.from_points(
        (Point(2, 3), Point(5, 6))) == Rectangle(2, 3, 5, 6)


def test_properties():
    rect = Rectangle(5, 6, 7, 8)

    assert rect.top == 8
    assert rect.bottom == 6
    assert rect.left == 5
    assert rect.right == 7
    assert rect.width == 2
    assert rect.height == 2
    assert rect.top_left == Point(5, 8)
    assert rect.top_right == Point(7, 8)
    assert rect.bottom_left == Point(5, 6)
    assert rect.bottom_right == Point(7, 6)
    assert rect.center == Point(6, 7)