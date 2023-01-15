# klasy w pythonie
import datetime


class Car:
    # lekcja 7
    # atrybut klasy - zmienne kontrolujace cale klasy
    carCount = 0

    # konstruktorem jest funkcja __init__  <<< dunder methods = double underscore methods = magic methods - wywoluja sie same w okreslonych przypadkach
    # self jest takim wskaznikiem zmiennej na instancje jej samej
    def __init__(self, brand, color):
        # print(self)
        self.brand = brand
        self.color = color
        # double dunder oznacza
        self.__serviceBook = [{1: '1-1-2023'},
                              ]

        # inkrementacja atrybutu
        Car.carCount += 1
        print('init...')

    # metody instancji <<< wywolujemu na istniejacych obiektach, self jest dostepny dla kazdej metody
    def info(self, date):
        print(f"""
      Brand: {self.brand}
      Color: {self.color}
      Datetime: {date}
      """)

    # to zostanie obsluzone domyslnie przez print, ladny string
    def __str__(self):
        return self.brand

    def __len__(self):
        return len(self.__serviceBook)
#############################


car1 = Car('bmw', 'black')
print(car1.brand)
car2 = Car('bmw', 'black')
car2.info(datetime.date.today())

# to niejako dodaje drugi atrybut o tej samej nazwie
car1.serviceBook = [
    {1: '1-1-2023'},
    {2: '1-2-2023'},
]
# car1.brand = 'Piotr'
# po double dunder to nie bedzie mozliwe
# setattr(car2, 'owner', 'Janusz')
print(vars(car1))

# =============================================

# doc string - dokumentacja klasy: dawaj typy wszedzie, komentuj - to potem jest widoczne w opisach metod!
# jak nazywa sie rozszerzenie generujace doc string? autoDocstring - python docstring generator
# kazda silownia ma atrybut miasto, slownik {'poznan': 2, 'wroclaw': 1}

# class Gym:
#     # atrybut klasy
#     gymCityDict = dict()
#     # konstruktor

#     def __init__(self, name, city, monthlyPrice, exercisesList):
#         self.name = name
#         self.city = city
#         self.monthlyPrice = monthlyPrice
#         self.exercisesList = exercisesList
#         # inkrementacja miast, metoda instancji to metoda wewnatrz klasy
#         try:
#             Gym.gymCityDict[city] += 1
#         except KeyError:
#             Gym.gymCityDict[city] = 1
#         print('gym init...')
#     def info(self)->None:
#         print(self)


# gym1 = Gym('PowerLift', 'Szczecin', '100zl', [
#            'power lifting', 'aerobic', 'joga'])
# print(Gym.gymCityDict)
# gym2 = Gym('PowerLift', 'Szczecin', '100zl', [
#            'power lifting', 'aerobic', 'joga'])
# print(Gym.gymCityDict)

# gym3 = Gym('PowerLift', 'Poznan', '100zl', [
#            'power lifting', 'aerobic', 'joga'])
# print(Gym.gymCityDict)
