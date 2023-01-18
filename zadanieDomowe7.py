# ; Zadania
# ; Todo app
# ; Stwórz aplikacje konsolowa do zarzadzania zadaniami do zrobienia (Todo-list).
# ; Daj użytkownikowi możliwość:
# ; 1. Dodac nowe zadanie
# ; 2. Zobaczyć liste zadań
# ; 3. Oznaczyć zadanie jako wykonane
# ; 4. Usunąć zadanie z listy
# ; 5. Eksport obecnego stanu listy do pliku formatu json
# ; 6. Import zadań z pliku formatu JSON (jako druga opcja dodania nowego/owych zadań)

# ; Co do eksportu:
# ; -gdy wybrano, zapytaj jak nazwać plik i zapisz listę zadań do pliku o podanej nazwie (format nadaj samodzielnie - json).

# ; Co do importu:
# ; -gdy wybrano, wyświetl dotychczas zapisane listy (wykorzystaj moduł os, aby przeskanować folder), zapytaj który plik użytkownik chce zaimportować. Po wybraniu dodaj zadania z wybranego pliku do aktualnie tworzonej listy.

import os
import pathlib
import json

# # sciezka do katalogu biezacego pliku i do jego rodzica (katalog glowny tego projektu)
dirPath = pathlib.Path(__file__).parent.resolve()
dataFilesDirPath = os.path.join(dirPath, 'dane')
tasks = list()

while (True):
    print(f"""
    Aplikacja ToDo do zadań:
    1. Dodaj nowe zadanie
    2. Zobacz liste zadań
    3. Oznacz zadanie jako wykonane
    4. Usuń zadanie z listy
    5. Eksport obecnego stanu listy do pliku formatu json
    6. Import zadań z pliku formatu JSON (jako druga opcja dodania nowego/owych zadań)
    7. Koniec programu (utrata danych bez zapisu)
    """)

    a = int(input('Podaj nr akcji: '))
    if (a == 1):
        # 1. Dodaj nowe zadanie
        task = input('Podaj treść zadania: ')
        tasks.append({'description': task, 'done': False})
    elif (a == 2):
        # 2. Zobacz liste zadań
        if len(tasks) == 0:
            print('Lista zadań pusta')
        else:
            print(tasks)
            print(f'''NUMER | WYKONANO | OPIS''')

            for index, task in enumerate(tasks):
                print(
                    f'''{index+1}.  | {task['done']}  | {task['description']}''')
    elif (a == 3):
        # 3. Oznacz zadanie jako wykonane
        index_task = int(
            input('Podaj numer zadania, ktore zostało wykonane: '))
        tasks[index_task-1]['done'] = True
    elif (a == 4):
        # 4. Usuń zadanie z listy
        index_task = int(input('Podaj numer zadania, ktore chcesz usunąć: '))
        del tasks[index_task-1]
    elif (a == 5):
        if len(tasks) == 0:
            print('Lista zadań pusta')
        else:
            # 5. Eksport obecnego stanu listy do pliku formatu json
            fileName = input('Podaj nazwę pliku do zapisu (rozszerzenie .json zostanie dodane) ')
            fullPath = os.path.join(dataFilesDirPath, fileName+'.json')
            try:
                with open(fullPath, mode='w', encoding='utf-8') as file:
                    json_string = json.dumps(tasks)
                    file.write(json_string)
            except OSError:
                print('Podany plik nie istnieje')    
    elif (a == 6):
        # 6. Import zadań z pliku formatu JSON (jako druga opcja dodania nowego/owych zadań)
        fileName = input('Podaj nazwę pliku do odczytu (rozszerzenie .json zostanie dodane) : ')
        fullPath = os.path.join(dataFilesDirPath, fileName+'.json')
        print(fullPath)
        try:
            with open(fullPath, mode='r', encoding='utf-8') as file:
                contents = json.loads(file.readline())
                for content in contents:
                    print(content)
                    tasks.append({'description': content['description'], 'done': content['done']})
                print(contents)
        except OSError:
            print('Podany plik nie istnieje')
    else:
        print('Koniec programu')
        break

# moznaby w wielu przypadkach inputow sprawdzac rodzaj danych - zarowno czy value sie zgadza jak i regex - czy nie wystepuja znaki specjalne tworzace dziwne pliki