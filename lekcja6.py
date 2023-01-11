#dane

# jsonowe dane
jsonString = """{
    "id": 7,
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "mailto:telly.hoeger@billy.biz",
    "address": {
      "street": "Rex Trail",
      "suite": "Suite 280",
      "city": "Howemouth",
      "zipcode": "58804-1099",
      "geo": {
        "lat": "24.8918",
        "lng": "21.8984"
      }
    },
    "phone": true,
    "website": null,
    "company": {
      "name": "Johns Group",
      "catchPhrase": "Configurable multimedia task-force",
      "bs": "generate enterprise e-tailers"
    }
  }"""

# pythonowe dane 
film = {
    "title": "Titanic",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ("Leonardo DiCaprio", "Rose Jones"),
    "budget": None,
    "credits": {
        "director": "Leonardo DiCaprio",
        "writer": "Alan Turner",
        "animator": "Anime Animatrix"
    }
}

#biblioteka do obslugi jsona
import json

from os.path import join

#serializacja 
#dump - dump - wyrzuca dane do pliku ,dumps - zamienia dane z pythona na string jsona
jsonFilm = json.dumps(film)

# jak zrobic zeby powstal folder jesli go nie bylo? obsluga bledow
folderPath = r'/Users/aleksanderdudek/Desktop/python-test/dane'
path = join(folderPath, 'titanic.json')

#os.mkdir jako obsluga bledu with open i wtedy jeszcze raz
with open(path, 'w', encoding='utf-8') as jsonFile:
    # zamienia string pythonowy na jsona
    json.dump(film, jsonFile)

#deserializacja - zamienia string jsonowy na dane pythonowe
#load - load json z pliku, loads - load danych w programie
pythonData = json.loads(jsonString)
print(pythonData)

path = r'/Users/aleksanderdudek/Desktop/python-test/dane/titanic.json'

with open(path, 'r', encoding='utf-8') as jsonFile:
    # zamienia jsona na string pythonowy
    titanicInfo = json.load(jsonFile)

print(titanicInfo)


 