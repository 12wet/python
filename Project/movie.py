from dataclasses import dataclass

class Movie():
    id: int
    title: str
    release_date: str
    director: str

    def __init__(self, id, title, director, release_date = None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.director = director

@dataclass
class MovieDao():
    title: str
    release_date: str
    director: str

    def __init__(self, title, director, release_date = None):
        self.title = title
        self.release_date = release_date
        self.director = director