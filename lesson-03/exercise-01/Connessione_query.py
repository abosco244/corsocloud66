# Tira fuori tutti gli attori che hanno partecipato al film african egg (nome, cognome)

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
    cursore.execute("select a.first_name, a.last_name from film f, actor a, film_actor fa where (f.film_id = fa.film_id and a.actor_id = fa.actor_id and f.title = 'AFRICAN EGG')")
    # get all records
    records = cursore.fetchall()
    print("Total number of rows in table: ", cursore.rowcount)

    print("\nPrinting each row")
    for row in records:
            print("Name = ", row[0])
            print("Lastname = ", row[1])
            
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connessione.is_connected():
        connessione.close()
        cursore.close()
        print("MySQL connection is closed")