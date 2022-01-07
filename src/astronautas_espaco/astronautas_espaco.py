import requests
from os import system, name

def clear():
    """Set clear screen command according OS type"""
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

clear() 
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)
print("Lista de astronautas atualmente no espaço\n")
for person in json['people']:
    print(person['craft'], ' - ', person['name'] )
    