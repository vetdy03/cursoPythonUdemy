import sqlite3

with sqlite3.connect("10-sqlite/app.db")  as con:# Connect to the SQLite database
    cursor = con.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER PRIMARY key, nombre VARCHAR(50));
        """
    )
