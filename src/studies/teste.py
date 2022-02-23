###########################################################
# Lista vazia
print("lista vazia")
print("-------------------------------------------------")
#
###########################################################
empty = []
print(empty)
print()





###########################################################
# list of strings
print("List of strings")
print("-------------------------------------------------")
#
############################################################
acronyms = ['lol', 'idk', 'tbk',]
print(acronyms)
print(acronyms[0]) #print lol
print()





###########################################################
# list update
print("Update list")
print("-------------------------------------------------")
#
############################################################
acronyms = ['lol', 'idk', 'tbk',]
acronyms[1] = 'rxt' # update list index 1
print(acronyms[1]) # print rxt
print()





###########################################################
# add list item
print("add list itens")
print("-------------------------------------------------")
#
############################################################
acronyms = ['lol', 'idk', 'tbk',]
acronyms.append('imho') # add item to the end of the list
print(acronyms)
print()





###########################################################
# remove list itens
print("Remove list itens")
print("-------------------------------------------------")
#
############################################################
acronyms = ['lol', 'idk', 'tbk','tmc', 'jdk', 'lsx']
acronyms.remove('lol') # remove item lol
print(acronyms)
acronyms.remove(acronyms[1])  # remove item of index 1
print(acronyms)
print()





###########################################################
# delete list itens
print("Delete list itens")
print("-------------------------------------------------")
#
############################################################
del acronyms[1] # same as line above
print(acronyms)
print()





###########################################################
# insert list itens
print("Insert list itens")
print("-------------------------------------------------")
#
############################################################
acronyms.insert(2, 'teste')
print (acronyms)
print()





###########################################################
# check if item exists
print("check list item existence")
print("-------------------------------------------------")
#
############################################################
if 'lol' in acronyms:
    print('True')
# check if item exists:
if 1 in [1,2,3,4]:
    print('True')
print()





###########################################################
#print list itens
print("Print list itens")
print("-------------------------------------------------")
#
###########################################################
for item in acronyms:
    print(item)
print()






###########################################################
#sum numbers
print("sum numbers")
print("-------------------------------------------------")
#
############################################################
numbers = [1,32,5,7]
print(sum(numbers))
print()





###########################################################
# mix types in lists
print("mix types in lists")
print("-------------------------------------------------")
#
###########################################################
anything = ['a',1,1.5]
print(anything)
print()





###########################################################
# Ordenando permanente uma lista com metodo sort
print("Ordenando lista permanente com sort")
print("-------------------------------------------------")
#
###########################################################
cars = ['bmw', 'fiat', 'vw', 'chevrolet']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print()




###########################################################
# Ordenando temporarimente uma lista funcao sort
print("temporarimente uma lista funcao sort")
print("-------------------------------------------------")
#
###########################################################
cars = ['bmw', 'fiat', 'vw', 'chevrolet']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)
print()



###########################################################
# Inverter ordem original de uma lista
print("Inverter ordem original de uma lista")
print("-------------------------------------------------")
#
###########################################################
cars = ['bmw', 'fiat', 'vw', 'chevrolet']
print(cars)
cars.reverse()
print(cars)
print()




###########################################################
# list of lists - bidimensional
print("lists of lists")
print("-------------------------------------------------")
#
###########################################################
lists_of_lists = [[1,2,3],['a','b'],[1,'x']]
print(lists_of_lists)
print()





###########################################################
#ranges
print("ranges")
print("-------------------------------------------------")
#
###########################################################
range(7)  # iterate 7 times  (zero to 6)
range(0,7,1) # 0 start, 7 stop, 1 step
range(2,14,2) # (2,4,6,8,10,12)






###########################################################
#ranges
print("lista de numeros com range")
print("-------------------------------------------------")
#
###########################################################
for value in range(1,7):
    print(value)  # vai imprimir de 1 a 6
print()





###########################################################
#ranges
print("lista de numeros com range e list")
print("-------------------------------------------------")
#
##########################################################
minha_lista = list(range(1,7))
print(minha_lista)
print()
print("pares de 2 a 10")
minha_lista2 = list(range(2,11,2))
print(minha_lista2)
print()



###
### range("primeiro numero", "vezes que irá interagir, frequencia")
###


###########################################################
## example: 
print("range example")
print("-------------------------------------------------")
#
###########################################################
total = 0
expenses = []
num_expenses = int(input("enter # of expenses: "))
for i in range (num_expenses):
    expenses.append (float(input("Enter a expense: ")))
total = sum(expenses)
print("total expenses is ", total)
print()



###########################################################
# get access acess for dictionary key and list item
#example
print("dictionary and lists examples")
print("-------------------------------------------------")
#
###########################################################
menus = {'breakfast': ['egg', 'bagel'],
         'dinner':    ['rice','beans']}

for name, menu in menus.items():
    print(name, ':', menu)
print()



###########################################################
# Dictionary to represent object
print("dictionary representing objects")
print("-------------------------------------------------")
#
###########################################################
person = {'name': 'Alan Santos', 
'city': 'Niteroi',
'age': '100',
'hobbies': ['music', 'guitar']}

print(person.get('name'), 'is', person.get('age'), 'years old')
print() 





###########################################################
# max min
print("max and min")
print("-------------------------------------------------")
#
###########################################################
numbers = [10,11,23,8,1000,4,3.5,23]
print(min(numbers))
print(max(numbers))
print()






###########################################################
# list comprehensions
print("lists comprehesions")
print("-------------------------------------------------")
#
###########################################################
squares = []
for value in range(1,11):
    squares.append(value **2 )
print(squares)

# list comprehension:
squares = [value ** 2 for value in range(1,11)]
print(squares)




