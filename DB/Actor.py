# Importazione del modulo MySQL
import mysql.connector
import DBUtility

class Actor:
   @classmethod
   def getAllActors(cls):
        connessione = DBUtility.getConnection()
        print(connessione)
        lista = list()
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database
            cursore.execute("select first_name, last_name from Actor")
            # get all records
            records = cursore.fetchall()
            print("Total number of rows in table: ", cursore.rowcount)

            print("\nPrinting each row")
            
            for row in records:
                    nome= row[0] 
                    cognome= row[1]
                    lista.add(nome,cognome)
            

        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
                print("MySQL connection is closed")
            return lista