# Stworz gre w wojne
# 1. Potasuj karty
# 2. Rozdaj karty 2 graczom (każdemu pięć kart) 
# 3. Porównuj karty po kolei dodajac punkty graczom (użyta karta ma znikać z talii - wykorzystaj metodę pop())
# 4. Wypisz wynik oraz zwycięzcę
# *w przypadku remisu nie dawaj punktu nikomu*
# *wykorzystaj liste poniżej jako talie* 
 
# cardList = ["9", "9", "9", "9",
#             "10", "10", "10", "10",
#             "Jack", "Jack", "Jack", "Jack",
#             "Queen", "Queen", "Queen", "Queen",
#             "King", "King", "King", "King",
#             "Ace", "Ace", "Ace", "Ace",
#             "Joker", "Joker"]

# Powodzonka i wesołych świąt!
from random import shuffle, randrange

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

cardListToValues = list()

# konwersja kart na wartosci liczbowe
for el in cardList:
    if el == '9':
        cardListToValues.append(9)
    if el == '10':
        cardListToValues.append(10)
    if el == 'Jack':
        cardListToValues.append(11)
    if el == 'Queen':
        cardListToValues.append(12)
    if el == 'King':
        cardListToValues.append(13)
    if el == 'Ace':
        cardListToValues.append(14)
    if el == 'Joker':
        cardListToValues.append(15)

player1Hand = list()
player2Hand = list()

player1Score = 0
player2Score = 0

# 1. Potasuj karty
shuffle(cardListToValues)

# 2. Rozdaj karty 2 graczom (każdemu pięć kart) 
for index in range(10):
    if index % 2 == 0:
        # zmniejszamy ilość kart w cardList
        player1Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
    else:
        # zmniejszamy ilość kart w cardList
        player2Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))

# 3. Porównuj karty po kolei dodajac punkty graczom (użyta karta ma znikać z talii - wykorzystaj metodę pop())

while(len(cardListToValues) > 0):
    # wyrzuc kartę z góry ręki czyli przyjmujemy index 0
    temp1 = player1Hand.pop(0) 
    temp2 = player2Hand.pop(0)
    
    # porownaj wyniki
    if temp1 > temp2:
        player1Score+=1
        print(f'Gracz 1: {temp1} Gracz 2: {temp2} Wygrywa: Gracz 1')
        player1Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        player2Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        continue
    elif temp1 < temp2:
        player2Score+=1
        print(f'Gracz 1: {temp1} Gracz 2: {temp2} Wygrywa: Gracz 2')
        player1Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        player2Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        continue
    else:
        print(f'Gracz 1: {temp1} Gracz 2: {temp2} Wygrywa: Remis')
        player1Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        player2Hand.append(cardListToValues.pop(randrange(0, len(cardListToValues))))
        continue

# 4. Wypisz wynik oraz zwycięzcę
print(f'''Tablica wyników:
Gracz1 - {player1Score} pkt 
Gracz2 - {player2Score} pkt
{ 'Wygrał gracz 1' if player1Score>player2Score else 'Wygral gracz 2' if player2Score>player1Score else 'Remis' }
''')

