import sqlite3

con = sqlite3.connect("10-sqlite/app.db")  # Connect to the SQLite database
cursor = con.cursor()  # Create a cursor object to execute SQL commands
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER PRIMARY key, nombre VARCHAR(50));
    """
)
con.commit() # commit los cambios y guardar la tabla
con.close()  # cierra la conexión
