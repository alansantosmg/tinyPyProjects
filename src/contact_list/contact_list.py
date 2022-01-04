"""Lista telefonica"""

from os import system

def show_interface():
    """Create the user interface"""

    # menu options
    menu = {
    1: "Adicionar contato",
    2: "Buscar contato",
    3: "Excluir contato",
    4: "Listar contatos",
    "x": "Sair"
}
    
    choice = ""
    while choice != "x":
        
        print("Contact List")  # Contact list title
        print()

        # Show user menu
        for menu_item in (menu):
            print("( {} ) {}".format(menu_item, menu[menu_item]), sep = " ")

        # input user option
        choice = str((input("Escolha sua opção: "))).lower()
        system("clear")
    
    print("bye!")  

def create_contact_list():
    contact_list = {}
    return contact_list
  

def add_contact(my_list):
    new_contact_name = str(input("Digite o nome do contato: "))
    new_contact_phone = str(input("Digite o telefone do contato: "))
    return my_list[new_contact_name] = new_contact_phone
    pass

def delete_contact():
    pass

def search_contact():
    pass

def show_contact_list(): 
    pass

def main():
    """main method"""

    system("clear")                 # clear screen
    mylist = create_contact_list()           # Create a new contact list
    show_interface()                # load user interface
    add_contact(mylist)


## call main 
if __name__ == "__main__":
    main()
















