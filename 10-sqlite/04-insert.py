import sqlite3

with sqlite3.connect("10-sqlite/app.db")  as con:# Connect to the SQLite database
    cursor = con.cursor() # crea un objeto cursor para ejecutar comandos SQL
    cursor.execute(
        "insert into usuarios values(?, ?) ", # pasar aqui los datos puede hackeado facilmente
        (10, "hola mundi"), 
    )