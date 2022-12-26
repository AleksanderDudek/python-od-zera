

# przerob to cwiczenie aby skorzystac ze zbiorów
# stworz dodatkowy zbior obecnych i korzystajac z operacji na zbiorach  wypisz
# obecnych i nieobecnych
# zrobić jezszcze operację logiczną na zbiorach

peopleList = {'Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Grzegorz Brzęczeszczykiewicz'}
presenceList = set()
yes_choices = ['yes', 'y', 'tak', 't', 'obecny']

for person in peopleList:
    presence = input(f'Czy {person} jest obecny? (obecny/nieobecny) ')
    if presence in yes_choices:
        presenceList.add(person)

for person in peopleList:
    isPresent = 'obecny' if (True if person in presenceList else False) else 'nieobecny'
    print(f'{person} jest {isPresent}')

