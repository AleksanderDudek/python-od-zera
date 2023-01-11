# Zadania:
# 1. Stworz prosty kalkulator podatkowy
# Użytkownik wprowadza kwote brutto 
try:
    a = float(input('Podaj kwotę brutto w zł: '))
    # oraz stawke podatku (np. 23%). 
    b = float(input('Podaj stawkę podatku w procentach % :'))
except ValueError as e:
    print(e)
else:
    # Na tej podstawie wypisz wartosc netto 
    try:
        netto = (100*a)/(100+b)
    except ZeroDivisionError as e:
            print(e)
    else:
        # oraz wartosc podatku.
        podatek = a - netto

        print(f'Stawka netto to: {round(netto,2)}, a podatek to {round(podatek,2)}')

