#pliki i obsluga bledow 

#try
#except
#else (optional)
#finally (optional)


# w try chcemy najmniej kodu, najlepiej 1-2 linijkowy


#modul os sluzy do relatywnych sciezek do pliku
#with, context manager

# Stworz liste zakupow w pythonie
# 1 - zobacz liste
# 2-dodaj produkt
# 3-usun produkt
# 4-zakoncz tworzenie i zapisz liste w pliku txt

import os
import pathlib

dirPath = pathlib.Path(__file__).parent.resolve() 

filePath = os.path.join(dirPath, 'zakupy.txt')

print(filePath)


# skonczyc liste zakupow!
a = 0
while(a != 4):
    a = int(input('''
    1 - zobacz liste
    2 - dodaj produkt
    3 - usun produkt
    4 - zakoncz tworzenie i zapisz liste w pliku txt
    '''))
    if(a == 1):
        try:
            with open(filePath,encoding='utf-8') as file:
                print(file)
        except FileNotFoundError as e:
                print(e)
    elif(a == 2):
        # czy plik istnieje? funkcja sprawdzajaca albo stworzyc pusty plik
            with open(filePath, mode='w' ,encoding='utf-8') as file:
                print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
    elif(a == 3):
            # odczyt pliku jako lista read().splitlines()
            # usunac z listy i zapisac liste w trybie w, 2 contexty
            print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
    elif(a == 4):
        print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
        break
