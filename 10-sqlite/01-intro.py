import sqlite3

con = sqlite3.connect("10-sqlite/app.db") # Connect to the SQLite database
con.close()  # Close the connection
