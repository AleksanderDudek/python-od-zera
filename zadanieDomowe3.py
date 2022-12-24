# #Zadania:
# # Lista obecnosci
# # Stworz liste osob
# peopleList = ['Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Grzegorz Brzęczeszczykiewicz']
# # nastepnie sprawdz obecnosc przy pomocy input obecny/nieobency
# presenceList = list()
# yes_choices = ['yes', 'y', 'tak', 't', 'obecny']
# # nieobecnych usuwaj z listy
# for person in peopleList:
#     presence = input(f'Czy {person} jest obecny? (obecny/nieobecny) ')
#     if presence in yes_choices:
#         presenceList.append(person)

# # na koniec wypisz liste obecnych
# print('Obecni: ')
# print(presenceList)


# przerob to cwiczenie aby skorzystac ze zbiorów
# stworz dodatkowy zbior obecnych i korzystajac z operacji na zbiorach  wypisz
# obecnych i nieobecnych

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

#czemu tu jest odwrotna kolejność przy for in ?