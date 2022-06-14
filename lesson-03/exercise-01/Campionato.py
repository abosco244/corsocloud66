class Campionato:
         
    # Imposta il dizionario
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
                print(self.__s)
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
    c = Campionato()
    n = int(input("Da quante squadre e' composto il campionato?"))
    for i in range(0, n):

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
            print("get_last_team: " + str(c.get_last_team()))
            print("squadra: " + str(squadra))
            print("p: " + str(p))

            s[squadra]=p

            c.delete_team(squadra)

            print(squadra+" con un punteggio di "+str(p)+" punti")

 

        #ripristina lo stato del campionato

        for k in s:

            c.add_team(k, s[k])

 

    #verifichiamo che il numero delle squadre e lo stato del campionato sia lo stesso di quello iniziale

    print("Il campionato e' formato da "+str(c.get_number_of_team())+" squadre")

    print(c)

 

# main()




# def run():
#     campionato = Campionato()
#     inp = int(input("Inserisci il numero di squadre di cui sarà composto il nostro campionato: "))
    
#     for i in range(inp):
#         team = str(input("Inserisci il nome della squadra: "))
#         score = int(input(f"Inserisci il punteggio della squadra {team}: "))
#         campionato.add_team(team, score)
        
#     squadra, p = campionato.get_first_team()
#     print("La squadra che ha vinto il campionato e' "+squadra+" con un punteggio di " + str(p) + " punti")
    
#     print(campionato.get_first_team())
#     print(campionato.get_last_team())
    
#     suqadra, punteggio = campionato.get_first_team()
    
#     for i in range(0,3):
        
#         squadra, p = c.get_last_team()

#         s[squadra]=p

#         c.delete_team(squadra)

#         print(squadra+" con un punteggio di "+str(p)+" punti")
        
        
    
        
# run()