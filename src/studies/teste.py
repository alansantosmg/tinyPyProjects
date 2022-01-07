
# empty list
empty = []

# list of strings
acronyms = ['lol', 'idk', 'tbk',]

print(acronyms[0]) #print lol
acronyms[1] = 'rxt' # update list index 1
print(acronyms[1]) # print rxt
acronyms.append('imho') # add item to the end of the list
acronyms.remove('lol') # remove item lol
acronyms.remove(acronyms[1])  # remove item of index 1
del acronyms[1] # same as line above


# check if item exists
if 'lol' in acronyms:
    print('True')
# check if item exists:
if 1 in [1,2,3,4]:
    print('True')

for item in acronyms:
    print(item)


numbers = [1,32,5,7]
sum(numbers)

anything = ['a',1,1.5]

lists_of_lists = [[1,2,3],['a','b'],[1,'x']]


range(7)  #iterate 7 times  (zero to 6)
range(0,7,1) # 0 start, 7 stop, 1 step
range(2,14,2) # (2,4,6,8,10,12)

for i in range(7) # iterate 7 times

## example: 

total = 0
expenses = []
num_expenses = int(input("enter # of expenses:"))
for i in range (num_expenses):
    expenses.append = (float(input("Enter a expense:")))
total = sum(expenses)
print(total)

### get access acess for dictionary key and list item

#example

menus = {'breakfast': ['egg', 'bagel'],
         'dinner':    ['rice','beans']}

for name, menu in menus.itens():
    print(name, ':', menu)

# Dictionary to represent object

person = {'name': 'Alan Santos', 
'city': 'Niteroi',
'age': '100',
'hobbies': ['music', 'guitar']}

print(person.get('name'), 'is', person.get('age'), 'years old')