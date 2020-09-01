import sqlite3

# connect to database
connection = sqlite3.connect('returns.db')

# create a cursor
cursor = connection.cursor()

