# Python veniva utilizzato per la programmazione procedurale (machine learning)
# procedurale (Codice che va dal basso verso l'alto) => Segue delle procedure

# lo scope globale si intende quando una classe e dichiarata nella route del codice, o banalmente una variabile 
# Ogni variabile ha un suo indirizzo di memoria (posizione di memoria)
# La memoria e fatta da byte

id = 1 # Scope globale

def ciao():
    id = 12
    messaggio = "Ciao mondo" # Scope locale
    print(messaggio)
    
def saluto():
    global id # Vado a richiamare la variabile globale id
    id = 10
    messaggio = "buongiorno"
    print(messaggio)
    


# "f" della print e un placeholder, serve per formattare la stringa


# Tutti i magic method si scrivono __nome__


# Classe
class Human:
    """"Define a human"""
    Default_age = 0 # Attributi di classe
    Default_eye_color = "brown"
    
    # self dice al costruttore che si fa carico dell'oggetto
    def __init__(self, name, age): # Costruttore
        self.name = name # Attributi di istanza
        self.age = age
        
    def sleep(self):
        """The human sleep"""
        print(f"{self.name} is sleeping, Zzz Zzz...")
        
    # Metodi di classe e metodi d'istanza
    # I metodi sono di istanza, e non di classe (a parte qualche eccezione)
    def eat(self, food):
        """The human eat"""
        
    # Questo metodo e un metodo di classe
    @classmethod
    def base(cls):
        return cls("Mario", 0)

# Oggetto
umano1 = Human("Mario", 22)
umano2 = Human("Mario", 22)

# @classmethod è il decoratore che si utilizza per creare i Metodi di Classe, e che 
# permette quindi di passare come parametro la Classe invece dell'Istanza.
mario = Human.base()

print(f"{umano1.Default_eye_color}, {umano2.Default_eye_color}")

umano1.Default_eye_color = "green" # modifica attributo tramite oggetto
Human.Default_eye_color = "blue" # modifica attributo tramite classe

# Output
# brown brown
# blue blue

print(f"{umano1.Default_eye_color}, {umano2.Default_eye_color}")



class Persona:
    
    def __init__(self, nome, cognome, eta, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.indirizzo = indirizzo
        
    def __str__(self): # Lo uso per formattare il testo come voglio io
        return f"Name: {self.name} \n Age: {self.age} \n"
        
    def profilo_personale(self):
        return fr"""
        nome: {self.nome}
        cognome: {self.cognome}
        eta: {self.eta}
        indirizzo: {self.indirizzo}
        """
                
    @classmethod   
    def from_string(cls, stringa, *args): # cls significa che sta lavorando sulla classe e non sull'istanza, quindi non sull'oggetto
        nome, cognome, eta, indirizzo = stringa.split("-")
        return cls(nome, cognome, eta, indirizzo, *args)
    

# class Insegnante(Persona):
    
#     def __init__(self, nome, cognome, eta, indirizzo, materia):
#         self.materia = materia
#         super(self, nome, cognome, eta, indirizzo)
        
    
ironman = "Tony-Stark-40-Torre Stark"
persona1 = Persona.from_string(ironman)
print(persona1.profilo_personale())




# Customer Container
# Implementiamo queste operazioni grazie ai magic method

class Dizionario:
    
    def __init__(self):
        self.dizionario = {}
        
    def add(self, chiave):
        self.dizionario[chiave.lower()] = self.dizionario.get(chiave.lower(), 0) + 1
        
    # def __getitem__(self, chiave):
        
        
        
# Properties
# getter e setter
class P: 
    def __init__(self,x): 
        self.x = x 
 
    @property 
    def x(self): # Metodo getter che ritorna il valore
        return self.__x 
 
    @x.setter 
    def x(self, x): # Metodo setter che imposta il valore
        if x < 0: 
            self.__x = 0 
        elif x > 1000: 
            self._x = 1000 
        else: 
            self.__x = x 

p = P(12) 
print(p.x) 
p.x = 15 
print(p.x) 
p.x = 1010 
print(p.x) 
p.x = -1 
print(p.x) 
p._x = -10 
print(p._x)
