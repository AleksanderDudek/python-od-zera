# zrobić jezszcze operację logiczną na zbiorach

peopleList = {'Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Grzegorz Brzęczeszczykiewicz'}
presenceList = set()
yes_choices = ['yes', 'y', 'tak', 't', 'obecny']

for person in peopleList:
    presence = input(f'Czy {person} jest obecny? (obecny/nieobecny) ')
    if presence in yes_choices:
        presenceList.add(person)

# ponizszego for'a zamieniam....
# for person in peopleList:
#     isPresent = 'obecny' if (True if person in presenceList else False) else 'nieobecny'
#     print(f'{person} jest {isPresent}')

# ... na operacje logiczna na zbiorach 

#to do - operacja

present = peopleList & presenceList
absent = peopleList - presenceList

for person in present:
    print(f'{person} jest obecny')

for person in absent:
    print(f'{person} jest nieobecny')