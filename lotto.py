import random


def lotto_ziehung(anzahl):
    kugeln = list(range(1, 46))      # Kugeln 1 bis 45
    gezogen = []
    letzte = 44                      # letzte Position im freien Bereich

    for i in range(anzahl):
        pos = random.randint(0, letzte)    # zufaellige Position im freien Bereich
        zahl = kugeln[pos]
        gezogen.append(zahl)

        kugeln[pos] = kugeln[letzte]       # letzte Kugel auf den freien Platz
        kugeln[letzte] = zahl              # gezogene Kugel ans Ende
        letzte = letzte - 1                # freier Bereich wird kleiner

    return gezogen


def lotto_statistik(gezogen, statistik):
    for zahl in gezogen:
        statistik[zahl] = statistik[zahl] + 1      # Zaehler erhoehen


def viele_ziehungen(anzahl_ziehungen):
    statistik = {}
    for zahl in range(1, 46):
        statistik[zahl] = 0

    for i in range(anzahl_ziehungen):
        gezogen = lotto_ziehung(6)
        lotto_statistik(gezogen, statistik)        # nach jeder Ziehung

    return statistik


zahlen = lotto_ziehung(6)
print("Lottozahlen:", zahlen)

alle = lotto_ziehung(45)
print("Test mit allen 45 Zahlen:", sorted(alle))

for anzahl in [1000, 10000, 100000, 1000000]:
    statistik = viele_ziehungen(anzahl)
    print("Statistik nach", anzahl, "Ziehungen:")
    print(statistik)
