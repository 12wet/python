from database_connector import db, cursor
from typing import List
from movie import Movie


def all_movies():
    cursor.execute("SELECT * FROM movies")
    results = cursor.fetchall()
    movies: List[Movie] = []
    for result in results:
        movies.append(to_movie(result))
    return movies


def movie_id(id: int):
    cursor.execute("SELECT * FROM movies WHERE id = {}".format(id))
    return to_movie(cursor.fetchone())


def movie_title(title: str):
    title = title.replace("_", " ")
    cursor.execute("SELECT * FROM movies WHERE lower(title) = '{}'".format(title))
    return to_movie(cursor.fetchone())


def movies_director(director: str):
    director = director.replace("_", " ")
    cursor.execute("SELECT * FROM movies WHERE lower(director) = '{}'".format(director))
    results = cursor.fetchall()
    movies: List[Movie] = []
    for result in results:
        movies.append(to_movie(result))
    return movies


def movies_date(date: str):
    cursor.execute("SELECT * FROM movies WHERE release_date = '{}'".format(date))
    results = cursor.fetchall()
    movies: List[Movie] = []
    for result in results:
        movies.append(to_movie(result))
    return movies


def add_movie(movie: Movie): 
    cursor.execute(
        "INSERT INTO MOVIES (title, release_date, director) VALUES('{0}', '{1}', '{2}')"
        .format(movie.title, movie.release_date, movie.director))
    db.commit()


def delete_by_id(id: int):
    cursor.execute(
        "DELETE FROM MOVIES WHERE id = {}"
        .format(id))
    db.commit()


def delete_by_title(title: str):
    title = title.replace("_", " ")
    cursor.execute(
        "DELETE FROM MOVIES WHERE lower(title) = '{}'"
        .format(title))
    db.commit()


def delete_by_director(director: str):
    director = director.replace("_", " ")
    cursor.execute(
        "DELETE FROM MOVIES WHERE lower(director) = '{}'"
        .format(director))
    db.commit()

def delete_by_date(date: str):
    cursor.execute(
        "DELETE FROM MOVIES WHERE release_date = '{}'"
        .format(date))
    db.commit()


def to_movie(result):
    print(result)
    return Movie(
        id = result[0],
        title = result[1],
        release_date = result[2],
        director = result[3]
    )