# pliki i obsluga bledow

# try
# except
# else (optional)
# finally (optional)


# w try chcemy najmniej kodu, najlepiej 1-2 linijkowy


# modul os sluzy do relatywnych sciezek do pliku
# with, context manager

# r - read (domyslny)
# w - write (zapis)
# a - append (dopisywania)
# TRYBY MNOGIE
# r+
# a+
# w+

# import os
# folder = r'/Users/peplaj/Desktop/korepetycje/aleksander/przyklady'

# filePath = 'pogoda.txt'
# fullPath = os.path.join(folder, filePath)
# print(fullPath)

# file = open(path, 'a')
# file.write('\nwiec bedzie bloto')
# file.close()


# with open(path) as file:
#     content = file.read()
# #file.close()
# print(content)

# enter - funkcja wywolywana na poczatku

# close - funkcja wywolywana na koniec


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
while (a != 4):
    a = int(input('''
    1 - zobacz liste
    2 - dodaj produkt
    3 - usun produkt
    4 - zakoncz tworzenie i zapisz liste w pliku txt
    '''))
    if (a == 1):
        try:
            with open(filePath, encoding='utf-8') as file:
                contents = file.readlines()
                print('Lista produktów:')
                for index, item in enumerate(contents):
                    print(f'{index+1}. {item}')
                # with robi domyslnie file.close()
        except FileNotFoundError as e:
                print(e)
    elif (a == 2):
        # pobierz dane
        product_input = input('Podaj produkt i opcjonalna notatke do niego: ')
        # czy plik istnieje? funkcja sprawdzajaca albo stworzyc pusty plik
        with open(filePath, mode='a', encoding='utf-8') as file:
                # zapisz dane do pliku
                file.write("\n"+product_input)
                print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
    elif (a == 3):
        try:
            # odczyt pliku jako lista read().splitlines()
            with open(filePath,encoding='utf-8') as file:
                contents = file.readlines()
                print(contents)
                print('Lista produktów:')
                for index, item in enumerate(contents):
                    print(f'{index+1}. {item}')
            # with robi domyslnie file.close()
            product_index = int(input('Podaj nr produktu do usuniecia: '))
            with open(filePath,mode='w', encoding='utf-8') as file:
                del contents[product_index]
                print(contents)
                for item in contents:
                    file.write(item)
            print('Lista produktów po usunieciu:')
            for index, item in enumerate(contents):
                print(f'{index+1}. {item}')
        except FileNotFoundError as e:
                print(e)
            # usunac z listy i zapisac liste w trybie w, 2 contexty
        print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
    elif(a == 4):
        print('Zakonczone tworzenie. Zapisane w pliku zakupy.txt')
        break

