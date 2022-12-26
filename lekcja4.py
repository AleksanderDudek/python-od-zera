from time import time
#comprehensions

#wyrazenie listowne - list comprehension
#wyrazenie zbioru - set comprehension
#z kwadratowych na wasate

# numbers = [
#     # 3. co chce zapisywac,wyrazenie, obliczenie 
#     number*1.2
#     # 1. w drugiej jest for, w prawej czesci range zakres nie jest brany pod uwage
#     for number in range(0,31)
#     # 2. opcjonalny warunek zwrotu, domyslnie True
#     if number % 2 == 0
# ]

# print(numbers)

#wyrazenia slownikowe - dictionary comprehension
# peopleList = ['Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Grzegorz Brzęczeszczykiewicz']

# userData = {
#     'name': '',
#     'phoneNumber': '',
#     'address': '',
# }

# users = {
#     # 2. potem z petli zwracam userId jako klucz, a userData jako wartość
#     userId: userData
#     # 1. najpierw petla
#     for userId in range(100)
# }

# people = {
#     index+1: peopleList[index]
#     for index in range(len(peopleList))
# }

# print(people)


#generator ("wyrazenie tupletu"), szybszy od listy => badania ponize, lista szybsza

# numbers = (
#     # 3. co chce zapisywac,wyrazenie, obliczenie 
#     number
#     # 1. w drugiej jest for, w prawej czesci range zakres nie jest brany pod uwage
#     for number in range(100000000)
#     # 2. opcjonalny warunek zwrotu, domyslnie True
# )
# start = time()
# for number in numbers:
#     result = number*2
# end = time()

# print(f'Generator: { end-start }s')

# numbers = [
#     # 3. co chce zapisywac,wyrazenie, obliczenie 
#     number
#     # 1. w drugiej jest for, w prawej czesci range zakres nie jest brany pod uwage
#     for number in range(100000000)
#     # 2. opcjonalny warunek zwrotu, domyslnie True
# ]
# start = time()
# for number in numbers:
#     result = number*2
# end = time()

# print(f'Lista: { end-start }s')

# numbers = (
#     number
#     for number in range(100)
# )

# print(next(numbers))
# print(next(numbers))
# print('-------------')

# for number in numbers:
#     print(number)
#     if number == 23:
#         break

# print('-------------')
# print(print(next(numbers)))

# # 3 imiona podac,
# names = list()
# # a = input('Podaj imię nr 1: ')
# # b = input('Podaj imię nr 2: ')
# # c = input('Podaj imię nr 3: ')

# # names.append(a)
# # names.append(b)
# # names.append(c)

# for _ in range(3):
#     a = input('Podaj imię: ')
#     names.append(a)

# #  tworze wyrazeniem slownikowym - kluczem imie, wartoscia dlugosc imienia
# namesDict = {
#     name: len(name)
#     for name in names
# }

# print(namesDict)

# people = [1, 3, [{
#     "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
#     "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
#     "yDlgcn99xPc19mYXcRmy": {'name': 'Pawel', 'age': 25, 'sex': 'Female'},
#     "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
#     "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
#     "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
#     "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
#     "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
#     "94cp4hsyZP2BnCh4D34z": {'name': 'Piotr', 'age': 25, 'sex': 'Female'},
#     "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
# }]]


# identificators = {'identificators': [
#     {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'Pawel', 'age': 27, 'sex': 'Male'},
#     {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
#     {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Piotr', 'age': 25, 'sex': 'Female'}
# ]}


# marks = {"marks": [
#     "Piotr", (2, 1, 2, 3, 2, 3),
#     "Pawel", (4, 2, 1, 3, 4)
# ]}

# # imie Marie z people
# print(people[2][0]['KQ4bir3y4tlkbG69I7zq']['name'])
# # imie Piotr z identificators
# print(identificators['identificators'][2]['name'])
# # oceny Pawła z marks
# print(marks['marks'][1])

# funkcje
# def greet(name, surname):
#     return (f'Hello {name} {surname}')

# print(greet('Aleksander', 'Dudek'))

# def get_males(people: list[str])->list[str]:
#     males = []
#     for person in people:
#         males.append(person) if person.split(' ')[0][-1] != 'a' else None
#     return males

# peopleList = ['Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Grzegorz Brzęczeszczykiewicz']

# print(get_males(peopleList))
# get_males()

# peopleList = ['Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni', 'Józek Wózek', 'Alina Wazelina', 'Jakub Piotr', 'Andrzej Wojcik', 'Alicja Galicja', 'Antoni Baroni','Grzegorz Brzęczeszczykiewicz']
# tuple = (1, 2, 3, 3, 3, 3)

# def remove_duplicates(people):
#     no_duplicate_list = set(people)
#     data_type = type(people)
#     return data_type(no_duplicate_list)

# print(remove_duplicates(peopleList))
# print(remove_duplicates(tuple))

#return konczy funkcje albo zwraca wartosc konczac funkcje

# defaultowe argumenty maja byc po domyslnych - dziwne
# def print_characters(amount: int, character: str = '-') -> str: #non-default args, default args
#     print(character*amount)

# print_characters(30, "'")
# print_characters(character="'", amount = 30) #positional args, keyword args korzystam jesli nie chce wszystkich argumentow uzyc 

#* robi z argumentu tuplet
def count_avg(total_time, *distance):
    return

# built-in functions
def calc_paint(eficiencyPerm2, *area):
    return eficiencyPerm2*sum(area)

print(calc_paint(2, 3,4,5,6))
print(calc_paint(2, 5,6))

# * tuplet, ** slownik
def name(*args, **kwargs):
   print(args)
   print(kwargs)

# kwargs - kluczem nazwa argumentu, wartoscia wartosc argumentu
name(1,2,3, dog='reksio')

def name_unpacked(*args, **kwargs):
   print(*args)
   print(*kwargs)

name_unpacked(1,2,3, dog='reksio')

#sprawdzic filter, map w built-in functions, modul random, shuffle, choice


