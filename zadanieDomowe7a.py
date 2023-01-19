# ; API
# ; https://api.stackexchange.com/docs
# ; Napisz program, który pozyska pytania zadane dnia dzisiejszego na temat pythona. 


# using calendar module
# using time module
import requests
from datetime import datetime, timedelta, date
import os
import pathlib
import json

# # sciezka do katalogu biezacego pliku i do jego rodzica (katalog glowny tego projektu)
dirPath = pathlib.Path(__file__).parent.resolve()
dataFilesDirPath = os.path.join(dirPath, 'dane')

dt = date.today()
midnight_today = datetime.combine(dt, datetime.min.time()).strftime('%Y-%m-%d')
minus_1_days = (dt - timedelta(days=1)).strftime('%Y-%m-%d')

stackApiUrlWithPython = f'https://api.stackexchange.com/2.3/search?fromdate={minus_1_days}&todate={dt}&order=desc&sort=activity&tagged=python&site=stackoverflow'
#  Wybierz 5 pytań, które zostały zadane przez użytkowników z największą reputacją.
req = requests.get(stackApiUrlWithPython)

try:
    unsorted_questions = list(req.json()['items'])

# sort elements by reputation
    sorted_by_rep_questions = sorted(unsorted_questions, key=lambda d: d['owner']['reputation'], reverse=True) 

    for index, item in enumerate(sorted_by_rep_questions):
        if (index > 5):
            break
        else:
            print(item['owner']['reputation'])
except:
    print('Blad api - sprobuj pozniej')
# pop 5 times

#  Zapisz je w słowniku {idKonta: linkDoPytania,...} 
output = {}
for_json_output = {}

for index, item in enumerate(sorted_by_rep_questions):
    if (index > 5):
            break
    else:
        # nie mogę zserializować takiego typu slownika w slowniku, czy jest jakis serializer lepszy?
        output[item['owner']['account_id']] = {'username': {item['owner']['display_name']}, 'reputation': item['owner']['reputation'] ,'link': {item['link']} }
        for_json_output[item['owner']['account_id']] = item['link']

print(output)
# i zapisz ten słownik do pliku w formacie json z i nazwij datą dnia dzisiejszego, np. 11-01-2021.json.
# ; Chodzi o to, aby można było ten program uruchomić każdego dnia i pozyskać pytania, które potrzebują odpowiedzi. 
fullPath = os.path.join(dataFilesDirPath, midnight_today+'.json')

with open(fullPath, mode='w', encoding='utf-8') as file:
    json_string = json.dumps(for_json_output)
    file.write(json_string)
