# Zadania
# Zbuduj funkcję mierząca szybkosc działania innych funkcji.
from time import time

def measure_function_time(func, *args) -> float:
    start = time()

    if not args: func() 
    else: func(*args)


    end = time()

    print(f'Czas działania to {end - start}s') 

def print_function(text: str) -> None:
    print(text)

def print_10_numbers() -> None:
    for index in range(0,10):
        print(index)

def print_range_numbers(left: int, right: int) -> list[int]:
    temp = list()
    for index in range(0,10):
        temp.append(index)
    return temp

# measure_function_time(print_function('lol'))
measure_function_time(print_function, 'lol2')
measure_function_time(print_10_numbers)
# measure_function_time(print_range_numbers(1,10))
measure_function_time(print_range_numbers, 1, 2)

# jak zmodyfikować, zeby przyjmowac takze wywolanie funkcji z argumentem? a nie tylko nazwe funkcji i parametry?

# Napisz funkcję zwracająca srednia przekazanych wartosci (dowolna ilosc argumentow)

# Stwórz grę w papier, kamień, nożyce

# Powodzenia!