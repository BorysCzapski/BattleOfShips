import random

makieta2 = [[' '] * 8 for x in range(8)]
makieta = [[' '] * 8 for x in range(8)]

litery_na_liczby = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def wypisz_plansze(plansza): #wypisuje plansze
    print("   A B C D E F G H")
    print("------------------")
    num_rzedu = 1
    for rzad in plansza:
        print("%d|%s" % (num_rzedu, "|".join(rzad))) # wypisuje rzedy w formacie 1| | | | | |, 2| | | | | | |   itd.
        num_rzedu += 1 

def stworz_statki(plansza): #
    for statek in range(5):
        rzad_statku,kolumna_statku = random.randint(0,7), random.randint(0,7)
        while plansza[rzad_statku][kolumna_statku] == "X":
            rzad_statku, kolumna_statku = random.randint(0,7), random.randint(0,7)
        plansza[rzad_statku][kolumna_statku] = 'X'

def lokalizacja_statku(): #zapytanie uzytkownika o rzad i kolumne
    rzad = input('Napisz numer rzedu 1-8')
    while rzad not in '12345678':
        print('Napisz poprawny numer')
    kolumna = input('Napisz numer kolumny A-H')
    while kolumna not in 'ABCDEFGH':
        print('Napisz poprawna kolumne')
    return int(rzad) - 1, litery_na_liczby[kolumna]

def policz_uderzone_statki(plansza): #liczy pokonane statki
    licznik = 0
    for rzad in plansza:
        for kolumna in rzad:
            if kolumna == "X":
                licznik += 1
    return licznik


stworz_statki(makieta2)
wypisz_plansze(makieta2)
kolejki = 10

while kolejki > 0:
    print('Witaj w grze w statki')
    wypisz_plansze(makieta)
    rzad, kolumna = lokalizacja_statku()
    if makieta[rzad][kolumna] == "-":
        print("Juz to zgadywales")
    elif makieta2[rzad][kolumna] == "X":
        print("Brawo trafiles w statek")
        makieta[rzad][kolumna] = 'X'
        kolejki -=1
    else:
        print("Nie trafiles")
        makieta[rzad][kolumna] = '-'
        kolejki -= 1
    if policz_uderzone_statki(makieta) == 5:
        print("Wygrales")
        break
    print("Masz " + str(kolejki) + " kolejek")
    if kolejki == 0:
        print("Przegrales")
        break
