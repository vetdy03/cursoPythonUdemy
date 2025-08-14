import sqlite3

with sqlite3.connect("10-sqlite/app.db")  as con:# Connect to the SQLite database
    cursor = con.cursor() # crea un objeto cursor para ejecutar comandos SQL
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchall())