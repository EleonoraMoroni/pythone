#identificare i caratteri Unicode che rappresentano i 4 semi del Poker (Cuori, Quadri , Fiori e Picche) nella variante solo bordo
#creare una stringa con i 4 semiCQFP


#PICCHE UTF8
solo_bytes = b"\xE2\x99\xA1"
stringa = solo_bytes.decode()
print(stringa)

#CUORI UTF8
solo_bytes = b"\xE2\x99\xA2"
stringa = solo_bytes.decode()
print(stringa)

#FIORI UTF8
solo_bytes = b"\xE2\x99\xA7"
stringa = solo_bytes.decode()
print(stringa)

#QUADRI UTF8
solo_bytes = b"\xE2\x99\xA4"
stringa = solo_bytes.decode()
print(stringa)

#semi raccolti UTF8
solo_bytes = b"\xE2\x99\xA1\xE2\x99\xA2\xE2\x99\xA7\xE2\x99\xA4"
stringa = solo_bytes.decode()
print(stringa)