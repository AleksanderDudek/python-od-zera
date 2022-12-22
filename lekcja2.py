#operatory porownania 

# == musi sie zgadzac typ i wartosc
# print(2=='2');
# print(2==2);
# print(2!='2');

# print(bool(''))
# print(bool([]))
# print(bool(0))


#instrukcje warunkowe
# a = int(input('Pass a number: '))
# b = int(input('Pass a number: '))

#albo albo
# if (b == 0):
#     result = None
# elif a == 0:
#     result = 0
# elif bool(a):
#     result = None
# else:
#     if True:
#         print('works')

#     result = a/b


# print(result)

# response = [1,2]

# if len(response) != 0:
#     print('nie pusta lista')
# if response:
#         print('nie pusta lista')

# a = int(input('Pass a number: '))
# b = int(input('Pass a number: '))

# if a % 2 == 0 and b != 0:
#     print(a/b)
# not to jsowy !

#zakres 1 - 30

# a = int(input('Pass a number: '))

# if (a > 0 and a <= 30):
#     print('Jest w przedziale 1-30')
# else:
#     print('Nie jest w przedziale 1-30')


#sprawdzac czy imie jest zenskie - 'a' na koncu
# a = input('Pass a name: ')

# if a[-1] == 'a':
#     print('Imie jest zenskie')
# else:
#     print('Nie jest imie zenskie')

#wybor czy chce pierwiastkowac czy wartosc bezwzgledna czy potega


#''' ''' pozwala na uzywanie entera 

# from math import sqrt


# a = int(input(''' Wybierz operację podając numer:
# 1. Pierwiastkuj podana liczbe.
# 2. Oblicz wartosc bezwzgledna podanej liczby.
# 3. Spoteguj liczbe. 
# '''))

# b = float(input('Podaj liczbe '))

# if a == 1:
#     result = sqrt(b)
# elif a == 2:
#     # ABSolute value
#     result = abs(b)
# elif a == 3:
#     c = float(input('Podaj potege '))
#     result = a**b
# else:
#     result = None

# print(result)

#wszystkie zmienne sa globalnie dostepne, nazywac je bardzo dokladnie, bo inaczej sie nadpisuja
#rozwiazaniem sa klasy i grupuje sie je w obiekty, kod jest czytany od gory do dolu
# importy, klasy, funkcje

#ternary, na koncu zawsze musi być wartość, one sa sekwen
# dayType = 1
# day = 'workday' if dayType == 1 else 'weekend' if dayType == 2 else 'holiday'

# rating = 5

# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')

# textRating = 'veryGood' if rating == 5 else 'good' if rating == 4 else 'weak'

#operacje ternary mozna wklejac jako wartosc 
# print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')


# price = 123
# bonus = 23
# bonus_granted = False

# if bonus_granted:
#     price -= bonus
# print(price)

# price -= bonus if bonus_granted else 0

#petle while i for 

# number = 0
# while number <= 10:
#     print(number)
#     number += 1



# from math import sqrt

# a=0
# while a != 4:
#     a = int(input(''' Wybierz operację podając numer:
#     1. Pierwiastkuj podana liczbe.
#     2. Oblicz wartosc bezwzgledna podanej liczby.
#     3. Spoteguj liczbe. 
#     4. Zakoncz program
#     '''))

#     if a == 4:
#         break

#     b = float(input('Podaj liczbe '))


#     if a == 1:
#         result = sqrt(b)
#     elif a == 2:
#         # ABSolute value
#         result = abs(b)
#     elif a == 3:
#         c = float(input('Podaj potege '))
#         result = b**c
#     else:
#         result = None
    

#     print(result)

#petla for od 1 do 10
# for number in range(1, 11, 1):
#     # print('Hello Aleksander')
#     print(number)

# print(f'Number after loop: {number}')

# konwencja jest taka ze to sie ma po prostu wykonac iles razy i tyle
# for _ in range(1, 11, 1):
#     print('Hello Aleksander')

#break - przerywa
#continue - przerywa iterację

#bankomat, balans zero, wplata, wyplata - nie ma debetu

# balans = 0;
# while (True):
#     a = int(input('''
#     Wybierz operację podając numer:
#     1. Balans konta
#     2. Wpłać pieniądze 
#     3. Wypłać pieniądze
#     4. Zakończ operacje
#     '''))

#     if(a == 1):
#         print(balans)
#     elif(a == 2):
#         b = int(input('Podaj kwotę wpłaty: '))
#         balans += b
#         print('Wplata pomyslna')
#     elif(a == 3):
#         c = int(input('Podaj kwote wyplaty: '))
#         if(balans - c < 0): 
#             print('Nie masz wystarczajacych srodkow do wyplaty')
#         else:
#             balans -= c
#             print('Srodki wyplacono') 
#     elif(a == 4):
#         break
#     else:
#         print('Bledny nr operacji')

#kolekcje 
# myList = [0, 1, 2, 'Iotr', True, None]
# myList = []
# myList = list()
# append dodaje na koniec listy
# myList.append('pies')
# myList.remove(True)
# pop usuwa automatycznie ostatni i zwraca go 
# print(myList.pop(-1))

# newList = myList[2:]
# print(myList)
# print(type(myList))
# print(newList)
# print('Iotr' in myList)
# print('Iotr' not in myList)