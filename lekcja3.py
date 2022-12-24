# # tuplet/krotka

# myTuple = (1, 2, 'Piotr')
# print(myTuple)

# # nie mozemy dodawac ani usuwac elementow, nie jest mutowalna
# # wszystie operacje na listach poza modyfikacja
# # co ma tuplet takiego fajnego? mam dane ktorych nie chce modyfikowac
# # oszczednosc miejsca na korzysc tupleta w tuplet vs lista
# # dane ktorych przez pomylke nie chce zmodyfikowac albo sa stale, odczyty z plikow, formularze

# print(type(myTuple))

#w tuplecie mozemy wpisac dane, ktorych nie chcemy uwzglednic albo uwzglednic w formularzu
#np. data wyslania formularza

# string
# exclude = ('data');
# tuplet, przecinek
# exclude = ('data',);

# print(type(exclude))

#set/zbior - tutaj duplikaty sa usuwane
# nie mozna indeksowac, mozna subskrybowac, mozna wykonywac operacje logicze jak w matematyce
# registry = {23, 132, 23, 123}
# registry.add(321)
# print(registry)

# myList = [1, 2,3,4,5,6,1,2,3,4,5,6]

# # rzutowanie zwraca niezalezny, nowy element w pamieci
# print(tuple(myList))
# print(set(myList))
# print(list(myList))

# #pusty set, to jest dictionary
# myDict = {}
# mySet = set()
# print(type(mySet))

#slownik - dict kluczem moze byc dowolna wartosc int, float, string , wartosciami moze byc dowolna wartosc, lista
# myDict2 = dict()
# users = {1: 'Piotr', 2: 'Jakub', 3:'Jacek'}


# defaultData = [ 'empty' ]
# # users = {
# #     id: defaultData
# #     for id in range(100)
# # }

# print(users)

# users[4] = 'Stefan' 
# users[4] += ' sss' 

# print(users)

# users.update({2: 'Ziutek', 4: 'Kamil'})

# print(users)

# del users[1]

# print(users)

# myList = range(1,5)
# for element in myList:
#     print(element)

# users = {1: 'Piotr', 2: 'Jakub', 3:'Jacek'}

# # wyswietla klucz
# for element in users:
#     print(element)

# # wyswietla klucz
# for element in users.keys():
#     print(element)

# # wyswietla wartosc
# for element in users.values():
#     print(element)

# # wyswietla tuplet klucz-wartosc
# for element in users.items():
#     print(element)

# # wyswietla tuplet klucz-wartosc
# for key, value in users.items():
#     print(key)
#     print(value)

# filmy - cena, przekaski - cena
# przeprowadzam przez kase

# total = 0
# films = {1: ('film1', 12),2: ('film2', 13),3: ('film3', 15)}
# snacks = {1: ('snack1', 12),2: ('snack2', 13),3: ('snack3', 15)}
# # filmy

# for key, (name, price) in films.items():
#         print(f'{key}. {name} cena {price} zł')

# a = int(input('Wybierz film (wprowadz numer): '))
# # przekaska
# for key, (name, price) in snacks.items():
#         print(f'{key}. {name} cena {price} zł')

# b = int(input('Wybierz przekąskę (wprowadz numer): '))

# total = (films[a])[1] + (snacks[b])[1]
# print(total)