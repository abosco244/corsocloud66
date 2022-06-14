class Persona:
    
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print(f"ciao sono {self.nome}")
        
class Insegnante(Persona):
    pass

persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri")