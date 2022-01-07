from os import system, name
import requests

def clear():
    """Set clear screen command according OS type"""
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

clear()

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:

    json_parsed = response.json()
    print("Cotação do dolar: R$", json_parsed['USDBRL']['high'],"\n")
else:
    print("Erro ao obter cotação. Response:", response.status_code)