# R8.16.

def conta(stringa):
   insieme = list(stringa) # ciao a voi" ==> {'c', 'i', 'a', 'o', ' ', 'v',}
   occorrenze = {} #dizionario chiave sarà la lettera, il valore in conteggio
   for lettera in insieme:
      occorrenze[lettera] = stringa.count(lettera)
   chiavi = list(occorrenze.keys())
   conteggi = list(occorrenze.values())
   valore_massimo = max(conteggi)
   return ([chiavi[conteggi.index(valore_massimo)]],
           set(list("abcdefghijklmnopqrstuvwxyz")) - set(chiavi),
           occorrenze)
   

saluto = "Ci vediamo puntuali domani mattina"
risultato = conta(saluto)
print(f"a) Le lettere più frequenti sono: {risultato[0]}")
print(f"a) Le lettere minuscole non presenti: {risultato[1]}")
print(f"a) Le occorrenze per ciascuna lettera: {risultato[2]}")

dizio = {"a": 5, "b": 4, "c": 5, "d": 2}

#max(dizio) #sottointende le chiavi , le lettere e quindi d

#max(dizio.values()) # fa una lista di valori darà 5, sia la a che la c
