# Si ha la necessità di gestire un campionato sportivo. In particolare, il campionato dovrà essere modellato 
# come una classe (in modo tale da poter istanziare campionati di diverse nazionalità) che contiene le due 
# informazioni fondamentali di ciascuna squadra del campionato: il nome e il punteggio ottenuto in campionato. 
# Non possono esserci due squadre con lo stesso nome all’interno dello stesso campionato. 
# NOTA: selezionare in modo opportuno la struttura dati che dovrà contenere le due informazioni relative 
# a ciascuna squadra e che dovrà essere contenuta nella classe campionato.

# Scrivere il programma Python che permette di definire le classi, gli attributi, le strutture dati e i metodi che:

# 1-inizializzano il campionato con un certo numero di squadre deciso dall’utente;
# 2-permettono di stabilire la squadra vincitrice del campionato e di visualizzarne le informazioni a schermo;
# 3-permettono di stabilire le ultime tre squadre in classifica e di visualizzarne le informazioni a schermo.
# Scrivere, inoltre, un breve main che mostri il funzionamento dei metodi definiti.



class Campionato:
    
    def __init__(self):
        self.squad = dict()
        
    def add_squad(self, name, score):
        self.squad[name] = score
        
    def get_first_squad(self):
        if len(self.squad) > 0:
            for key in self.squad:
                maxim = max(self.squad.values())                
                return maxim, maxim[key]
               
# campione = Campionato()

# c = []

# c.append(campione.add_squad("milan", 10))
# c.append(campione.add_squad("inter", 11))
# c.append(campione.add_squad("juve", 12))

# print(campione.get_first_squad())
# print(campione)
        
# def main():     
#     campione = Campionato()
#     numero_squadre = int(input("Da quante squadre e' composto il campionato? "))
#     squad_list = []
    
#     for i in range(0, numero_squadre):
#         nome_squadra = input("Inserire il nome della squadra: ")
#         squad_list.append(nome_squadra)
#         punteggio = int(input("Inserire il punteggio ottenuto dalla squadra " + nome_squadra + ": "))
#         campione.add_squad(nome_squadra, punteggio)
        
#     print(f"\n\nIl campionato e composto dalle seguenti squadre {squad_list}")
    
#     squadra, punteggio = campione.get_first_squad()
    
#     print("Il primo in classifica del campionato e' " + squadra + ", con un punteggio di " + str(punteggio))
    
# main()











class Campionato:
    
    

    def __init__(self):

        self.__s = dict()

    

    def add_team(self, nome, punteggio):

        self.__s[nome] = punteggio

    

    def get_team(self, nome):

        self.__s.get(nome,-10)

    

    def delete_team(self, nome):

        self.__s.pop(nome, 0)

    

    def get_first_team(self):

        if len(self.__s)>0:

            m=max(self.__s.values())

            for key in self.__s:

                if self.__s[key]==m:

                    return key, m

        else:

            return "",0

    

    def get_last_team(self):

        if len(self.__s)>0:

            m=min(self.__s.values())

            for key in self.__s:

                if self.__s[key]==m:

                    return key, m

        else:

            return "",0

    

    def get_number_of_team(self):

        return len(self.__s)

    

    def __str__(self):

        return str(self.__s)
    
    
    
    


def main():
        
    c = campionato.Campionato()

    n = int(input("Da quante squadre e' composto il campionato? "))

    for i in range(0,n):

        nome_squadra = input("Inserire il nome della squadra: ")

        punteggio = int(input("Inserire il punteggio ottenuto dalla squadra "+nome_squadra+": "))

        c.add_team(nome_squadra, punteggio)

    print("Il campionato e' formato da "+str(c.get_number_of_team())+" squadre")

    if c.get_number_of_team()>1:

        squadra, p = c.get_first_team()

        print("La squadra che ha vinto il campionato e' "+squadra+" con un punteggio di "+str(p)+" punti")

    if c.get_number_of_team()>0:

        print("Le ultime 3 squadre del campionato sono:")

        #s servirá per ripristinare tutte le squadre cancellate 

        s = dict()

        for i in range(0,3):

            squadra, p = c.get_last_team()

            s[squadra]=p

            c.delete_team(squadra)

            print(squadra+" con un punteggio di "+str(p)+" punti")

 

        #ripristina lo stato del campionato

        for k in s:

            c.add_team(k, s[k])

 

    #verifichiamo che il numero delle squadre e lo stato del campionato sia lo stesso di quello iniziale

    print("Il campionato e' formato da "+str(c.get_number_of_team())+" squadre")

    print(c)

 

main()