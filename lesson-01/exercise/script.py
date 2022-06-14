# ESERCIZIO 1
bool = True

while bool:
    x = input("Inserisci un numero:\n")
    if x:
        lastX = int(x)
        if lastX < 0:
            print(f"Il valore {lastX} e negativo")
            continue
        elif lastX == 0:
            print(f"Il valore di x e {lastX}")
        else:
            if lastX % 2 == 0:
                print(f"{lastX}")
        
        another = str(input("Vuoi inserire un altro numero? (SI o No)"))
        if another.upper() == "SI":
            bool = True
        else:
            bool = False
    else:
        print("Non hai inserito nessun numero") 
        continue
        
      
      
# ESERCIZIO 2  
age = int(input("Quanti anni hai? "))
patente = bool(input("Hai la patente? (SI oppure premi ENTER) "))

if age < 18:
    print(f"La tua età minore di {age}")
    
elif age >= 18:
    print(f"La tua età maggiore uguale di {age}")
    if patente == True:
        print("Puoi comprare la macchina\n")
    else:
        print("Però non hai la patente\n")
        
        
        
   
# ESERCIZIO 3  
bool = True
ingresso = True

ticket_adulto = 10
ticket_bambino = 10
ticket_anziano = 10

ticket_totali = ticket_adulto or ticket_anziano or ticket_bambino

age = int(input("Inserisci la tua età\n"))

if age < 18 and age > 1:
    print("Hai accesso al biglietto per bambini")
    
elif age >= 18 and age < 60:
    print("Hai accesso al  biglietto per adulti")
    
elif age >= 60 and age < 122:
    print("Hai accesso al biglietto per anziani")
    
else:
    print("Non hai inserito l'età correttamente")
    
    
if ticket_totali != 10:
    bool = True
    ticket = int(input("Quanti biglietti vuoi prendere?\n"))

    while(bool):
        if ticket > 10:
            print("Non puoi comprare così tanti biglietti")
            bool = True
        else:
            ticket_totali -= ticket
            bool = False

    if ticket <= ticket_adulto and ticket <= ticket_bambino and ticket <= ticket_anziano:
        print(f"Numero di biglietti acquiestati: {ticket}")
        print(f"Numero di biglietti disponibili {ticket_totali}")
else: 
    print("Ci scusiamo per il disguido ma non può procedere all'acquiesto del biglietto")