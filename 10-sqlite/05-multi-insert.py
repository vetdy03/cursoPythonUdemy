import sqlite3

with sqlite3.connect("10-sqlite/app.db")  as con:# Connect to the SQLite database
    cursor = con.cursor() # crea un objeto cursor para ejecutar comandos SQL
    usuarios = [
        (2, "Juan"),
        (3, "Ana"), 
        (4, "Pedro"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?) ",
        usuarios
    )