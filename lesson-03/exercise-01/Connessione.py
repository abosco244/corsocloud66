# Importazione del modulo MySQL
import mysql.connector

try:
    # Connessione a MySQL
    connessione = mysql.connector.connect(
    # Parametri per la connessione
    host="localhost",
    user="root",
    password="root",
    database="SAKILA"
    )
    print(connessione)
    # Generazione del cursore
    cursore = connessione.cursor()
    # Comando SQL per la visualizzazione dei database
    cursore.execute("select first_name, last_name from Actor")
    # get all records
    records = cursore.fetchall()
    print("Total number of rows in table: ", cursore.rowcount)

    print("\nPrinting each row")
    for row in records:
            print("First name = ", row[0] )
            print("Last name = ", row[1])
            #print("Lastname = ", row[2])
            
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connessione.is_connected():
        connessione.close()
        cursore.close()
        print("MySQL connection is closed")