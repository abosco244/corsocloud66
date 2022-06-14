import random

class Campionato:
         
    # Imposta il dizionario
    def __init__(self):
        self.__s = dict()
    
    def add_team(self, nome, punteggio):
        self.__s[nome] = punteggio

    def add_team_empty_score(self, nome):
        self.__s[nome] = 0

    def set_random_score(self):
        for key in self.__s.keys():
            self.__s[key] = random.randint(1, 50)
            
    def range_distance_team(self):
        first_team = self.get_first_team()
        last_team = self.get_last_team()
        return f"La distanza massima tra {first_team[0]} e {last_team[0]} è di {first_team[1] - last_team[1]} punti"
                              

    def get_team(self, nome):
        self.__s.get(nome,-10)
 
    def delete_team(self, nome):
        self.__s.pop(nome, 0)
 
    def get_first_team(self):
        if len(self.__s)>0:
            m=max(self.__s.values())
            for key in self.__s:
                print(self.__s)
                if self.__s[key]==m:
                    return [key, m]
        else:
            return "",0
 
    def get_last_team(self):
        if len(self.__s)>0:
            m=min(self.__s.values())
            for key in self.__s:
                if self.__s[key]==m:
                    return [key, m]
        else:
            return "",0
 
    def get_number_of_team(self):
        return len(self.__s)
 
    def __str__(self):
        return str(self.__s)













