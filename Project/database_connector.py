import sqlite3

database = "movies_database.db"

db = sqlite3.connect(database)

cursor = db.cursor()