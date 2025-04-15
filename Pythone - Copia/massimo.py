# acquisire una serie di num interi adottando un valore sentinella
# per terminar4e la lettura ('input()'), quindi print i l valore massimo p.60 - 186 q valore sentinella

prova = []
userInput = input("Inserisci un numero: ")
while userInput != "q":
    prova.append(int(userInput))
    userInput = input("Inserisci un numero: ")
temp = None
for v in prova
    if temp == None:
        temp  = v
    else: 
        if temp < v:
            temp = v
print("valore max", max(prova)) 
