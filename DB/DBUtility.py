from mimetypes import init
# Importazione del modulo MySQL
import mysql.connector
#host = 	34.175.195.122
#datbase =	dtdb (altrimenti lasciare vuoto il campo)
#user =	dtdb-user	| root	| digitaltraining
#pswdb = 	testtest1
class DBUtility:
    endpoint="localhost"
    user="root"
    password="Password01!"
    database="SAKILA"
    

    def getConnection(self):
        print("creo la connessione")  
        connessione=None      
        try:
            # Connessione a MySQL
            connessione = mysql.connector.connect(
            # Parametri per la connessione
            host=self.endpoint,
            user=self.user,
            password=self.password,
            database=self.database)
            print(connessione)
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        return connessione

        
        
        





    