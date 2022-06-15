from DBConnection import DBConnection
import mysql.connector

class Actor(DBConnection):

    def get_all_actors(self):
        connessione = DBConnection()
        connessione = connessione.get_connection()
        try:
            cursore = connessione.cursor()
            cursore.execute("select a.first_name, a.last_name from film f, actor a, film_actor fa where (f.film_id = fa.film_id and a.actor_id = fa.actor_id and f.title = 'AFRICAN EGG')")
            records = cursore.fetchall()
            for row in records:
                print("Name = ", row[0] + "\nLastname = ", row[1])
        except mysql.connector.Error as e:
                print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
                print("MySQL connection is closed")