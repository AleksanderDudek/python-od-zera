
# 2. Stworz generator haseł działający wg podanych kryteriów
# Haslo musi zawierac:
# -male litery
# -wielkie litery

# Hasło może zawierać(pytaj użytkownika co chce uwzglednic):
# -numery
# -znaki specjalne

# Dlugosc hasła wybiera użytkownik
# dlugosc hasla musi byc w zakresie <8;24> znaki (min 8 max 24 znaki)
# Aby pytać użytkownika o wartosci wykorzystaj funkcję input.
from random import randint

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

#biblioteka string - mozna zaimportowac te zbiory
small_letters = list(range_char('a', 'z'))
big_letters = list(range_char('A', 'Z'))
special_signs = list(range_char('!', '/')) + list(range_char(':', '@')) + list(range_char('{', '~'))
digits = list(str(range(0,10)))

print('Witaj w generatorze haseł. Hasło ma długość od 8 do 24 /n błędne dane w przypadku pytań tak/nie traktowane są jako negatywna odpowiedź ')

user_input1 = input('Czy hasło ma zawierać numery? (tak/nie): ')
user_input2 = input('Czy hasło ma zawierać znaki specjalne? (tak/nie): ')
try:
    user_input3 = int(input('Jaką długość ma mieć hasło? (przedział <8;24>): '))
except:
    print('Błędne dane')

yes_choices = ['yes', 'y', 'tak', 't']
no_choices = ['no', 'n', 'nie']
range_choices = list(range(8,25))

opt1 = False
opt2 = False
length = user_input3

# obsługa błędów 
# zrobić na while
if user_input1.lower() in yes_choices:
    opt1 = True
if user_input2.lower() in yes_choices:
    opt2 = True

if user_input3 not in range_choices:
    print('Błędne dane')
    exit()

#ostateczna generacja hasła na bazie opcji
#losowość osiągniemy na bazie wykonywania wszystkich zadanych instrukcji z tabeli w losowej kolejności

#generuj tabele moźliwości
signs_to_be_used = small_letters + big_letters 

if(opt1):
    signs_to_be_used += digits
if(opt2):
    signs_to_be_used += special_signs

print(signs_to_be_used)

#wygeneruj minimalne spełnienie zasady , tu jest git

# mozna robic to na stringu i appendowac
password = list(range(0, user_input3))

#pozbyc sie ponizej
#funkcja walidacyjna + funkcja generujaca haslo
#początek łańcucha z minimalnymi zasadami
password[0] = small_letters[randint(0, len(small_letters))] 
password[1] = big_letters[randint(0, len(big_letters))]
password[2] = special_signs[randint(0, len(special_signs))] if opt1 else signs_to_be_used[randint(0, len(signs_to_be_used))]
password[3] = digits[randint(0, len(digits))] if opt1 else signs_to_be_used[randint(0, len(signs_to_be_used))]

#reszta znaków bardziej losowo
#funkcja choice z modulu random
for _ in range(user_input3-4):
    password.append(signs_to_be_used[randint(0, len(signs_to_be_used))])

# tego mozna by sie pozbyc gdyby wyzej byl string
finalPasswod = ''.join(password)

print(f'Twoje wygenerowane hasło o długości {len(password)} to: {finalPasswod}')