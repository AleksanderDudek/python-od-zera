# Zadanie
# 1.
# Podaj, ile jest w pliku liczby.txt takich liczb, których cyfry pierwsza i ostatnia są takie same. 
# Zapisz tę z nich, która występuje w pliku liczby.txt jako pierwsza. W pliku z danymi jest co najmniej 
# jedna taka liczba. Odpowiedź dla danych z pliku przyklad.txt: 26 626 (26 takich liczb, które mają 
# pierwszą i ostatnią cyfrę taką samą; pierwszą z nich w pliku przykładowym jest 626).

import os
import pathlib

# # sciezka do katalogu biezacego pliku i do jego rodzica (katalog glowny tego projektu)
dirPath = pathlib.Path(__file__).parent.resolve()

def check_same_digits(number:int) -> tuple:
    numbers_digit_nmuber = len(str(number))
    is_single_digit_number = numbers_digit_nmuber == 1

    if(is_single_digit_number):
        return (True, number)
    elif(numbers_digit_nmuber>1):
        if(str(number)[0] == str(number)[numbers_digit_nmuber-1]):
            return (True, number)
        else:
            return (False, number)
    else:
        return (False, number)

def get_solution(filePath: str):
    try:
        with open(filePath, encoding='utf-8') as file:
            #zczytuje wszystkie liczby
            occurences = list()
            contents = file.readlines()
            for number in contents:
                # sprawdzam warunki zadania
                result = check_same_digits(int(number))
                # jesli spelniam warunek
                if(result[0]==True):
                    # dodaje liczbe do listy
                    occurences.append(result[1])
            # zwracam pierwsze wystapienie i ilosc tych samych liczb 
            # with robi domyslnie file.close()
    except FileNotFoundError as e:
            print(e)
    print(f'''W pliku wystepuje {len(occurences)} liczb, których pierwsza i ostatnia liczba są takie same. Pierwsza z nich to {occurences[0]}''')


#sciezka do liczby.txt
numbersFilePath = os.path.join(dirPath, 'liczby.txt')

get_solution(numbersFilePath)

#sciezka do przyklad.txt
exampleFilePath = os.path.join(dirPath, 'przyklad.txt')

get_solution(exampleFilePath)

# Zapisz tę z nich, która występuje w pliku liczby.txt jako pierwsza.

# ======================================================================
# 2.
# Znajdź w pliku liczby.txt:
# - liczbę, która ma w rozkładzie najwięcej czynników pierwszych (podaj tę liczbę oraz liczbę jej czynników pierwszych)
# - liczbę, która ma w rozkładzie najwięcej różnych czynników pierwszych (podaj tę liczbę oraz liczbę jej różnych czynników pierwszych).
# Przykład: liczba 420=2·2·3·5·7 ma w rozkładzie 5 czynników pierwszych, w tym 4 różne czynniki pierwsze (2, 3, 5, 7).
# Odpowiedź dla danych z pliku przyklad.txt: 144 6 210 4
# (Liczba 144 ma najwięcej czynników pierwszych; liczba czynników pierwszych liczby 144 wynosi 6. Liczba 210 ma najwięcej różnych 
# czynników pierwszych; liczba różnych czynników pierwszych liczby 210 wynosi 4).

# def count_prime_factors(number: int) -> int:
#     prime_factors_array = list()
#     temp = number
#     p = 2
#     while temp>=p*p:
#         if temp % p == 0:
#             temp = temp / p
#             print(f'temp {temp} prime {p}')
#             prime_factors_array.append(p)
#         else:
#             p+=1
#     print(prime_factors_array)
#     return len(prime_factors_array)

import math


def count_prime_factors(number: int) -> tuple:
    prime_factors_array = list()
    temp = int(number)
    p = 2
    while p <= math.sqrt(temp):
        while temp % p == 0:
            temp = temp / p
            prime_factors_array.append(p)   
        p+=1
    prime_factors_array.append(p)

    # 0 - ilosc czynnikow pierwszych, 1 - wszystkie czynniki pierwsze, 2 - ilosc unikalnych czynnikow pierwszych, 3 - unikalne czynniki pierwsze
    return (len(prime_factors_array), prime_factors_array, len(list(set(prime_factors_array))), list(set(prime_factors_array)))

# to jest do dopracowania - moze byc kilka liczb z taka sama iloscia czynnikow pierwszych, wiec trzeba sprawdzac do skutku ostatni element tablicy
def get_solution2(filePath: str) -> tuple:
    try:
        with open(filePath, encoding='utf-8') as file:
            #zczytuje wszystkie liczby
            max_number_of_prime_factors = 0
            max_numuber_of_different_prime_factors = 0
            list_of_m_n_o_p_f = list()
            list_of_m_n_o_d_p_f = list()

            contents = file.readlines()
            for number in contents:
                # sprawdzam warunki zadania
                result = count_prime_factors(int(number))
                # jesli spelniam warunek najwiecej czynnikow pierwszych
                if(result[0] > max_number_of_prime_factors):
                    # dodaje liczbe do listy, ostatni element ma najwieksza liczbe czynnikow pierwszych
                    list_of_m_n_o_p_f.append((result[0], int(number)))
                    max_number_of_prime_factors = result[0]
                # jesli spelniam warunek najwiecej czynnikow pierwszych
                if (result[2] > max_numuber_of_different_prime_factors):
                    # dodaje liczbe do listy, ostatni element ma najwieksza liczbe roznych czynnikow pierwszych
                    list_of_m_n_o_d_p_f.append((result[2], int(number)))
                    max_numuber_of_different_prime_factors = result[2]
    except FileNotFoundError as e:
            print(e)
    print(f'''Najwięcej czynników: {max_number_of_prime_factors} ma liczba: {list_of_m_n_o_p_f[-1][1]}. Najwięcej unikalnych czynników: {max_numuber_of_different_prime_factors} ma liczba {list_of_m_n_o_d_p_f[-1][1]}''')

# sciezka do liczby.txt
numbersFilePath = os.path.join(dirPath, 'liczby.txt')

get_solution2(numbersFilePath)

#sciezka do przyklad.txt
exampleFilePath = os.path.join(dirPath, 'przyklad.txt')

get_solution2(exampleFilePath)

# wyniki nie sa jednolicie prawidlowe, nie wiem jeszcze co jest 5?
# czy to wina algorytmu?
# print(count_prime_factors(288))