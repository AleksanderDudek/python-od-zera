
# Napisz funkcję zwracająca srednia przekazanych wartosci (dowolna ilosc argumentow)
def average_from_numbers(*args):
    if not args: 
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        return sum(args)/len(args)

print(average_from_numbers())
print(average_from_numbers(1.5))
print(average_from_numbers(1,2,3,4,5,6.6))

# Stwórz grę w papier, kamień, nożyce

# Powodzenia!