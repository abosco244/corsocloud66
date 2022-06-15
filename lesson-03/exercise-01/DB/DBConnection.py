import mysql.connector

class DBConnection:
        
    def get_connection(self):
        try:
            connessione = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="SAKILA"
            )
            return connessione
        
        except mysql.connector.Error as e:
            return "Error reading data from MySQL table", e