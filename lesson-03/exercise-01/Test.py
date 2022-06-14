from Campionato import Campionato

def main():
    c = Campionato()
    n = int(input("Da quante squadre e' composto il campionato?"))
    for i in range(0, n):

        nome_squadra = input("Inserire il nome della squadra: ")

        #punteggio = int(input("Inserire il punteggio ottenuto dalla squadra "+nome_squadra+": "))

        #c.add_team(nome_squadra, punteggio)

        print(c.add_team_empty_score(nome_squadra))

    c.set_random_score()

    print("Il campionato e' formato da "+str(c.get_number_of_team())+" squadre")

    print(c.range_distance_team())

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

 

main()