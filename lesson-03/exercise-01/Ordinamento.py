from Campionato import Campionato
from random import randint

class Ordinamento:

    def __init__(self, campionato: Campionato):
        self.squadra_punteggio = eval(str(campionato))
        self.ordina_dizionario()

    def ordina_dizionario(self):

        self.squadra_punteggio = {
            k: v for k, v 
            in sorted(
                self.squadra_punteggio.items(),
                key=lambda item: item[1],
                reverse=True
                )
        }  # ordina il dizionario per punteggio decrescente
    
    def mostra_n_squadre(self, numero):

        for n,p in self.squadra_punteggio.items():
            if numero < 1:
                break
            print(n,p)
            numero -= 1

    

def main():
    campionato = Campionato()
    popola_campionato(campionato)
    ordinamento = Ordinamento(campionato)
    ordinamento.mostra_n_squadre(5)


def popola_campionato(campionato: Campionato):
    nomi_squadre = ["Roma", "Lazio", "Viterbo", "Reggio Calabria", "Venezia"]
    nome_punteggio = { nome:randint(0,1000) for nome in nomi_squadre }
    for nome, punteggio in nome_punteggio.items():
        campionato.add_team(nome, punteggio)


if __name__ == "__main__":
    main()
