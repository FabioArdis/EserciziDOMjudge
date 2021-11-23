#   Esercizio:          N41 DOMjudge
#   Data creazione:     23/11/2021  09:46:14
#   Ultima modifica:    23/11/2021  14:51:51

#   Spiegazione esercizio:
#   Una compagnia aerea ci ha chiesto di programmare un sistema di prenotazione automatica
#   dei voli. Scrivere un programma che assegni i posti di ogni volo dell’unico aereo posseduto
#   dalla compagnia. Trovate il resto delle istruzioni nel pdf su DOMjudge.

#   Nota no.1
#   L'output e il testo stampato durante l'attesa dell'input devono essere tassativamente uguali 
#   a quelli che ho inserito, altrimenti DOMjudge darà problemi. Esatto, NON va usato end = ""
#   negli argomenti della funzione print(). Fate prima a copincollare.

#   Due liste, da 5 elementi ciascuna. 0 = posto libero, 1 = posto occupato.
fumatori    = [0, 0, 0, 0, 0]
nonFumatori = [0, 0, 0, 0, 0]

#   Variabili booleane necessarie per la condizione di loop.
fumatoriPieno       = False
nonFumatoriPieno    = False


#   Funzione che gestisce i posti dei fumatori.
def funcFumatori():

    #   Perché MAI Python vuole che dichiariamo UN'ALTRA VOLTA le variabili globali?
    #   Altrimenti pensa che siano locali. Mah, non vedo l'ora di ritornare a C++.
    global fumatoriPieno

    #   Contatore che sfrutteremo come indice della lista.
    contatore = 0

    #   Loop principale della funzione.
    for posto in fumatori:

        #   Controlliamo se l'elemento della lista (il posto) è 1(occupato)/0(libero),
        if posto == 0:

            #   Abbiamo trovato un posto libero, occupiamolo.
            fumatori[contatore] = 1
            print("Reparto fumatori, posto", contatore + 1)

            #   Controlliamo se il contatore è arrivato alla fine della lista, ergo i posti sono esauriti.
            if contatore + 1 == len(fumatori):
                fumatoriPieno = True

            #   Usciamo bruscamente dal nostro loop di controlli, tanto abbiamo trovato il nostro posto.
            break

        if posto == 1:
            #   Abbiamo controllato l'n posto, e pare che sia occupato. Andiamo avanti.
            contatore += 1


#   Funzione che gestisce i posti dei non fumatori.
def funcNonFumatori():

    #   Ripeto, odio Python
    global nonFumatoriPieno

    #   Contatore che sfrutteremo come indice della lista.
    contatore = 0

    #   Loop principale della funzione.
    for posto in nonFumatori:

        #   Controlliamo se l'elemento della lista (il posto) è 1(occupato)/0(libero),
        if posto == 0:

             #   Abbiamo trovato un posto libero, occupiamolo.
            nonFumatori[contatore] = 1
            print("Reparto NON fumatori, posto", contatore + 6)

            #   Controlliamo se il contatore è arrivato alla fine della lista, ergo i posti sono esauriti.
            if contatore + 1 == len(fumatori):
                nonFumatoriPieno = True
            
            #   Usciamo bruscamente dal nostro loop di controlli, tanto abbiamo trovato il nostro posto.
            break

        #   Abbiamo controllato l'n posto, e pare che sia occupato. Andiamo avanti.
        if posto == 1:
            contatore += 1


#   La nostra funzione principale, chiamatela come vi pare. 
def main():

    #   Ri-dichiariamo un'altra volta le nostre due amate variabili globali
    global fumatoriPieno
    global nonFumatoriPieno

    #   Chiediamo all'utente l'input
    scelta = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))

    #   Agiamo in base alla scelta. Non viene gestito il misinput, come dettato dal pdf.
    if scelta == 1:

        #   Controlliamo che ci sia almeno un posto vuoto.
        if not fumatoriPieno:
            funcFumatori()

        #   Altrimenti diamo all'utente la possibilità di cambiare reparto.
        else:
            scelta = str(input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?"))

            #   Gestiamo il reindirizzamento attraverso un comando via input.
            if scelta == "S":
                funcNonFumatori()
            else:
                print("Il prossimo volo parte tra 3 ore")

    if scelta == 2:

        #   Controlliamo che ci sia almeno un posto vuoto.
        if not nonFumatoriPieno:
            funcNonFumatori()

         #   Altrimenti diamo all'utente la possibilità di cambiare reparto.
        else:
            scelta = str(input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?"))

            #   Gestiamo il reindirizzamento attraverso un comando via input.
            if scelta == "S":
                funcFumatori()
            else:
                print("Il prossimo volo parte tra 3 ore")


#   Finchè entrambi i reparti non saranno pieni, richiamiamo la nostra funzione principale.
while not(fumatoriPieno == True and nonFumatoriPieno == True):
    main()
