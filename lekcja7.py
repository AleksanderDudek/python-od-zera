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
        return f"""
      Brand: {self.brand}
      Color: {self.color}
      """

    def __len__(self):
        return len(self.__serviceBook)

    #metoda klasy, argumentem jest klasa - zazwyczaj jako kreator obiektow
    @classmethod
    def createFromString(cls, stringArgs):
        args = stringArgs.split(',')
        return cls(args[0], args[1])
    
    #metody klasy, metody instancji, metody statyczne

    #metody statyczne 
    @staticmethod
    def convertKMhToMph(kmh) -> float:
        return kmh*0.6 

#############################

class Truck(Car):
    def __init__(self, brand: str, color: str, capacity: float):
        super().__init__(brand, color)
        self.capacity = capacity

    def info(self):
        super().info('dddd/mm/')
        print(f'Capacity: {self.capacity}t')

    # mozna sie takze odwolac do np. __str__ , __len__

    def __str__(self):
        super().__str__()
truck1 = Truck('man', 'white', 4.5)
print(truck1)

# =============================================

car1 = Car('bmw', 'black')
print(car1.brand)
car2 = Car('bmw', 'black')
car2.info(datetime.date.today())

# to niejako dodaje drugi atrybut o tej samej nazwie, ale nie jest hermetyczna wlasciwoscia klasy
car1.serviceBook = [
    {1: '1-1-2023'},
    {2: '1-2-2023'},
]
# car1.brand = 'Piotr'
# po double dunder to nie bedzie mozliwe
# setattr(car2, 'owner', 'Janusz')
print(vars(car1))

car3 = Car.createFromString('audi, red')
print(vars(car3))

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
