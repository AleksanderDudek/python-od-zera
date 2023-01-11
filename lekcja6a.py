#requests
import requests

# #api endpoints
# urlUsers = 'https://jsonplaceholder.typicode.com/users'
# r = requests.get(urlUsers)

# # lista pythonowa, przetwarzanie
# print(type(r.json()))

# content = r.json()

# #formatowanie
# users = {}
# for person in content:
#   users[person['id']] = person['username']

# print(users)

#utworz slownik gdzie kluczami jest ID userow, a wartosciami to ilosc zadan, ktore dany user wykonal 

urlToDos = 'https://jsonplaceholder.typicode.com/todos'
tasks = requests.get(urlToDos).json()

userTasks = {}

# for userTask in tasks:
#   try:
#     userTasks[userTask['userId']] = userTasks[userTask['userId']] + (1 if userTask['completed'] else 0)
#   except KeyError:
#     userTasks[userTask['userId']] = 0

for userTask in tasks:
  if userTask['completed']:
    try:
      userTasks[userTask['userId']] += 1
    except KeyError:
      userTasks[userTask['userId']] = 1

print(userTasks)

#potem znajdz liste uzytkownikow z najwieksza liczba wykonanych zadan

# sprawdzam max w slowniku
# ustalam max score
#keys() values() items()
maxScore = max(userTasks.values())
bestScoreUsersIds = []

print(maxScore)

for key, score in userTasks.items():
    if score == maxScore:
      bestScoreUsersIds.append(key)

print(bestScoreUsersIds)

usersUrl = 'https://jsonplaceholder.typicode.com/users'

bestScoreUsersUsernames = []

for userId in bestScoreUsersIds:
  username = requests.get(f'{usersUrl}/{userId}').json()['username']

print(bestScoreUsersUsernames)