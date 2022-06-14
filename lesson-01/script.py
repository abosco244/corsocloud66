from pickle import FALSE, TRUE


print("Hello world!")

# Tipi di dato
# int, float char, str

# I nomi devono sempre essere i più descrittivi possibili

print("1" + "1")


x = input("Inseriscici un input:\n")



# Aggiornare il risparmio personale di un utente dopo l'inserimento del risparmio corrente settimanale

risparmio = 1000

bool = True

while(bool):
    aggiungi = int(input("Aggiungi il risparmio:\n"))
    totale = risparmio + aggiungi
    print(totale)
    
    anotherAdd = str(input("Vuoi aggiungere altri risparmi? (SI o NO)"))
    
    if(anotherAdd.upper == "SI"):
        bool = True
    else:
        bool = False





# Operatore //
# Ti ritorna il resto della divisione togliendo il decimale




# Formattazione
nome = 'Mario'
cognome = 'Rossi'
nome_completo = f'{nome} {cognome}'
print(nome_completo)


# METODI PER LE STRINGHE
# capitalize() => restituisce una copia della stringa con il solo carattere iniziale maiuscolo
# upper() => restituisce una copia della stringa convertita in maiuscolo
# lower() => restituisce una copia della stringa convertita in minuscolo
# find() => trova la prima occorrenza del valore specificato
# strip() => restituisce una copia della stringa senza gli spazi all'inizio e alla fine della stringa
# replace("old", "new") => restituisce una copia della stringa con tutte le occorrenze della sottostringa old sostituite da new



x = 10
y = 5

if x < y:
    print(f"{x} è maggiore di {y}")
    
print("fine")

x = 5
y = 10

if x < y:
    print(f"{x} è maggiore di {y}")
    
print("fine")





x = 5
y = 10

if x < y:
    print(f"{x} è maggiore di {y}")
elif x > y:
    print(f"{x} è minore di {y}")
    
print("fine")





x = 10
y = 10

if x < y:
    print(f"{x} è maggiore di {y}")
elif x > y:
    print(f"{x} è minore di {y}")
else:
    print(f"{x} è uguale a {y}")
    
print("fine")





for counter in range(5):
    print(f"tentativo numero {counter}")
    
    
# range (stop)
# range (start, stop)
# range (start, stop, range/step)



# Ciclo while, break e continue
x = 100
while x > 0:
    x -= 30
    print(x)
print("Fine ciclo")


# break
x = 100
while x > 0:
    x -= 30
    if x == 10:
        break # Interrompe
    print(x)
print("Fine ciclo")


# continue
x = 100
while x > 0:
    x -= 30
    if x == 10:
        continue # Smette di eseguire il singolo blocco e ritorna alla condizione
    print(x)
print("Fine ciclo")




# Liste
# Serie ordinata di dati
list = [1, 2, "casa", 3.14, True]

# Le liste hanno delle proprietà
a = ['a', 'b']
b = ['c', 'd']
c = a + b

# Accecere agli elementi della lista
a[0]

a[0] = 'nuovo'


# Unpacking
# Metodo utilizzato per prendere un singolo elemento da una lista
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
primo, *altri, secondo = list2
print(primo, altri, secondo)

""" *altri => ha lo stesso effetto dello spread operator """
# Output => primo = a, altri = [b, c, d, e], secondo = f


# Ciclare una lista
lettere = ['a', 'b', 'c']

for lettera in enumerate(lettere):
    print(lettera)
    
    
# insert, pop, append, remove, index
lettere.insert(1, 'g')
lettere.append('h')

# sort
lista4 = ['a', 'b', 'c', 'd']
lista4.sort()
print(lista4)




# Tuple
# Sono come le liste, ma sono solo in lettura, questo significa che non possiamo modificarle





# Dizionario
dizionario = {33: 'giulio', 22: 'luca'}
print(dizionario)


# Per cancellare una chiave
# del



# for key in diz
# for x in diz.items:
# for key, value in diz.item









# Funzioni
# Esempio di funzione print e len

def somma(x, y): # parametri della funzione
    s = x + y;
    return s

somma(10, 5) # argomenti della funzione



def saluto(): # funzione di tipo void
    print('ciao')
    
saluto()


def somma(*addendi): # Lo usiamo quando non sappiamo quanti parametri avrà la nostra funzione
    totale = 0
    for valore in addendi:
        totale += valore
    return totale

print(somma(5, 7, 3, 6))



def anagrafica(**utente):
    print(utente)
    
anagrafica(nome = "mario", cognome = "rossi", eta = 33)




# Variabili globali e locali
id = 1
def ciao():
    messaggio = "ciao mondo"
    print(messaggio)
    
def saluto():
    messaggio = "buongiorno"
    print(messaggio)
    
    
    
    
    
    
    
# Tipi di strutture dati
# str, int, float, bool
# list[], tuple(), range(), set{}, dict{k:v}


x = "5"
y = 5
print(x + y) # Darà errore

x = "5"
y = "5"
print(x + y) # Darà "55"

x = 5
y = 5
print(x + y) # Darà 10


# Casting
x = "5"
y = 5
print(int(x) + y) # Darà 10
print(x + str(y)) # Darà "55"


# Escape
x = "ciao dall\'altra parte"

z = "ciao sono Luca"
# Slicing di una stringa
print(z[0:5]) # Prenderà la stringa da 0 a 5 => ciao

# Metodi stringhe
# len(), upper(), find(), replace()
print(z.upper())
print(len(z))
print(z.find('Luca'))
print(z.replace('Luca', 'Marco'))



# Operatori matematici
# + - * / % ** //
a = 10
b = 5
print(a + b) # somma
print(a - b) # sottrazione
print(a * b) # moltiplicazione
print(a / b) # divisione
print(a % b) # modulo
print(a ** b) # potenza
print(a // b) # divisione senza resto

import math

c = -5
d = [4, 3, 2, 1]

print(math.sqrt(a))
print(abs(c))
print(math.max(d))
print(math.min(d))




# Condizioni short-end
if b > 10 : print("E maggiore di 10")
print("E maggiore di 10") if b > 10 else print("E minore di 10")


