# Importazione del modulo MySQL
import mysql.connector

try:
    # Connessione a MySQL
    connessione = mysql.connector.connect(
    # Parametri per la connessione
    host="localhost",
    user="root",
    password="Password01!",
    database="SAKILA"
    )
    print(connessione)
    # Generazione del cursore
    cursore = connessione.cursor()
    # Comando SQL per la visualizzazione dei database
    cursore.execute("select * from Actor")
    # get all records
    records = cursore.fetchall()
    print("Total number of rows in table: ", cursore.rowcount)

    print("\nPrinting each row")
    for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Lastname = ", row[2])
            
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connessione.is_connected():
        connessione.close()
        cursore.close()
        print("MySQL connection is closed")