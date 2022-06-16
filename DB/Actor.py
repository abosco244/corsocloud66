# Importazione del modulo MySQL
import mysql.connector
from DBUtility import DBUtility

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

    # Task 1
    @staticmethod
    def getMoviesByActor(first_name, last_name):
        connessione = DBUtility.getConnection()

        try:
            cursore = connessione.cursor()
            query = """SELECT f.title
                            FROM actor a, film f, film_actor fa
                            WHERE f.film_id = fa.film_id
                            AND a.actor_id = fa.actor_id
                            AND a.first_name = %s
                            AND a.last_name = %s"""
            cursore.execute(query, (first_name, last_name))

            """Extract the resulting table from the processed query"""
            return cursore.fetchall()
        except mysql.connector.Error as e:
            print("\nError reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()

    # Task 2
    @staticmethod
    def getMoviesByYear(first_name, last_name, order=False):
        connessione = DBUtility.getConnection()
        order = 'ASC' if order else 'DESC'

        try:
            cursore = connessione.cursor()
            query = f"""SELECT f.release_year, f.title
                            FROM actor a, film f, film_actor fa
                            WHERE f.film_id = fa.film_id
                            AND a.actor_id = fa.actor_id
                            AND a.first_name = %s
                            AND a.last_name = %s
                            ORDER BY f.release_year {order}"""
            cursore.execute(query, (first_name, last_name))

            """Extract the resulting table from the processed query"""
            return cursore.fetchall()
        except mysql.connector.Error as e:
            print("\nError reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()

    # Task 3
    @staticmethod
    def getActorsByDirector(director):
        connessione = DBUtility.getConnection()

        try:
            cursore = connessione.cursor()
            query = """SELECT DISTINCT a.first_name, a.last_name
                            FROM actor a, film f, film_actor fa
                            WHERE f.film_id = fa.film_id
                            AND a.actor_id = fa.actor_id
                            AND f.director = %s"""
            cursore.execute(query, (director, ))

            """Extract the resulting table from the processed query"""
            return cursore.fetchall()
        except mysql.connector.Error as e:
            print("\nError reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()