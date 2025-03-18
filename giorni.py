giorni(
    "lunedi   " + #0        (1-1)*9
    "martedi  " + #9        (2-1)*9
    "mercoledi" + #18       (3-1)*9
    "giovedi  " + #27       (4-1)*9
    "venerdi  " + #36       (5-1)*9
    "sabato   " + #45       (6-1)*9
    "domenica "   #54       (7-1)*9
)

giorno = int(input("indica giorno: "))
p = (giorno - 1) * 9
print(giorno[p:p+9])
