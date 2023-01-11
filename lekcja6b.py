# klasy w pythonie
import datetime 
class Car:
  # konstruktorem jest funkcja __init__  <<< dunder methods = double underscore methods - wywoluja sie same w okreslonych przypadkach
  # self jest takim wskaznikiem zmiennej na instancje jej samej
  def __init__(self, brand, color):
    print(self)
    self.brand = brand
    self.color = color
    print('init...')
  
  # metody instancji <<< wywolujemu na istniejacych obiektach, self jest dostepny dla kazdej metody
  def info(self, date):
    print(f"""
      Brand: {self.brand}
      Color: {self.color}
      Datetime: {date}
      """)
#############################

car1 = Car('bmw', 'black')
print(car1.brand)
car2 = Car('bmw', 'black')
car2.info(datetime.date.today())

# class Gym:
#     # konstruktor
#     def __init__(self, name, city, monthlyPrice, exercisesList):
#       self.name = name
#       self.city = city
#       self.monthlyPrice = monthlyPrice
#       self.exercisesList = exercisesList
#       print('gym init...')

# gym1 = Gym('PowerLift', 'Szczecin', '100zl', ['power lifting', 'aerobic', 'joga'])

