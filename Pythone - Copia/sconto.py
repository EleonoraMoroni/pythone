def discount(prices, isPet, nItems):
    SCONTO_APPLICATO = 0.2
    if (nItems == 0 or
        nItems < 6 or
        len(set(isPet)) == 1):
        return 0.00;
    i = 0
    cnt = 0
    somma = 0.00
    while i < nItems:
        if not isPet[i]:
            somma += prices[i]
            cnt += 1
        i += 1
    if cnt >= 5:
        return somma * SCONTO_APPLICATO
    else:
        return 0.00

nItems = 0
prices = []
isPet = []
cassiera = input("Scrivi il prezzo dell'articolo, finisci con y se è un animale, con n se è un articolo: ")
cassiera [0:cassiera.find(" ")]
cassiera [-1]
while cassiera != "-1":
    prices.append(float(cassiera[0:cassiera.find(" ")]))
    isPet.append(cassiera[-1] == "y")
    nItems += 1
    cassiera = input("Scrivi il prezzo dell'articolo, finisci con y se è un animale, con n se è un articolo: ")

