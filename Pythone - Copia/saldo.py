# es P5.22 pag 334 - Scrivere una funzione che calcoli il saldo
# di un conto bancario dopo che sia no trascorsi una dato numero
# di anni a partire da un dato saldo iniziale e con un dato tasso
# di interess eannu , accreditando gli interesse annuo,
# accreditando gli interessi annualmente

def saldo(saldo_iniziale, tasso, numero_di_anni= None) :
    if numero_di_anni == None :
        # stampare 20 valori del saldo anno dopo anno
       saldo_iniziale = 0
       saldo_totale = 0
       tasso = 0.04
       saldo_iniziale = input("Inserisci il saldo iniziale: ")
       i = 0
       for i = 20 :
          saldo_totale = (saldo_iniziale + (saldo_iniziale * tasso)) * i
        saldo()

    #    pass
   # else :
        # restituisco (return) il saldo richiesto
       # pass