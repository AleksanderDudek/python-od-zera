# Zadania:
# 1. Stworz prosty kalkulator podatkowy
# Użytkownik wprowadza kwote brutto 
a = float(input('Podaj kwotę brutto w zł: '))
# oraz stawke podatku (np. 23%). 
b = float(input('Podaj stawkę podatku w procentach % :'))
# Na tej podstawie wypisz wartosc netto 

netto = (100*a)/(100+b)
# oraz wartosc podatku.
podatek = a - netto

print(f'Stawka netto to: {round(netto,2)}, a podatek to {round(podatek,2)}')

