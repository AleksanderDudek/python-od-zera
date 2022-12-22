#importowanie paczek, optymalizacja pod katem wybranych metod
from math import sqrt

# zmienne - calkowite, zmiennoprzecinkowe
a = 4.5 #float
b = 4 #int
c = 4j #complex 
d = '' + ""
e = "Format'ed text"
f = 'text'
# dzielenie zawsze daje wynik float np. 8 / 2 = 2.0
g = True 
h = False #duze liter
i = None #pusty, nie istnieje

#operatory 
# * mnozenie, / dzielenie, % modulo, ** potegowanie

print(3**5)


teamA = ['Piotr', 'Aleksander']
teamB = ['Jakub', "Stefan"]
teamC = [1, 2, 3]

# po prostu lista
print(teamA+teamB)

# mieszana lista, nie ma znaczenia
print(teamA+teamC)

#typy - nie narzuca typow, troche smieszne 
def get_fuel(avgBurn: float, distance: int) -> int:
    return avgBurn*distance;

#rzutowanie

#mozna wyswietlic string * liczba 
print(get_fuel(10, '1'))

#indeksowanie i slicing 

#klasycznie od 0 jest indeksowane, mozna indeksowac stringa
print(teamA[0][3])

#indeks od tylu
print(teamA[0][-3])

#slicing, lewostronnie domkniete
print(teamB[0][2:-1])

print(type(d))

print(sqrt(20))

print(round(sqrt(20), 5))

array = [] #0, ''
print(bool(array))