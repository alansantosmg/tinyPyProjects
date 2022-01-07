"""Console rock paper and scissors game

Usage:
    python3 rps_game.py
"""


import random
from os import system, name


# global player options dict
OPTIONS = {"p": "pedra","a":"papel","t":"tesoura"}


def computer_player_option():
    """ get computer game option

        Args:

        Returns: 
            A string of random computer choice from the options list.    
    """
    return random.choice(list(OPTIONS.values()))


def user_choice_option():
    """ Set humans player option
        
        Args: 
        
        returns:
            The user_prompt string
    """
    # reload user options case invalid selection
    user_choice_loop = None
    while user_choice_loop == None:

        # show human player options
        clear()
        print("\nOi! Vamos jogar?\n")   
        
        for option in (OPTIONS):
            print("( {} ) {}".format(option, OPTIONS[option]), sep = " ")

        # prompt user
        user_prompt = input('\nPedra, papel ou tesoura? Digite a sua opção: ').lower()
        
        # return a valid selected option
        if OPTIONS.get(user_prompt) != None:
            return OPTIONS.get(user_prompt)        
            

def game_choices(user_choice, computer_choice):
    """ Show player's option

        Args: 
            user_choice string, computer_choice string
    """ 
    print()
    print("computador ---->",computer_choice.upper(), "x", user_choice.upper(),"<---- Jogador" )
    print()


def game_result(user_choice, computer_choice):
    """ Show the game result

        Args: 
            user_choice string, computer_choice string
    """
    if computer_choice == user_choice:

    ## TODO: use dictionary for game turn messages
        print('Ixi! Deu empate!')
    elif computer_choice == "papel" and user_choice == "tesoura":
        print("Tesoura corta papel. Você ganhou!")
    elif computer_choice == "papel" and user_choice == "pedra":
        print("Papel embrulha pedra. Você perdeu!")
    elif computer_choice == "tesoura" and user_choice == "pedra":
        print("Pedra quebra tesoura. Você ganhou!")    
    elif computer_choice == "tesoura" and user_choice == "papel":
        print("Tesoura corta papel. Você perdeu!")
    elif computer_choice == "pedra" and user_choice == "Papel":
        print("Papel embrulha pedra. Você ganhou!")
    elif computer_choice == "pedra" and user_choice == "tesoura":
        print("Pedra quebra tesoura. Você perdeu!")
    elif user_choice == "papel" and computer_choice == "tesoura":
        print("Tesoura corta papel. Você perdeu!")
    elif user_choice == "papel" and computer_choice == "pedra":
        print("Papel embrulha pedra. Você ganhou!")
    elif user_choice == "tesoura" and computer_choice == "pedra":
        print("Pedra quebra tesoura. Você perdeu!")  
    elif user_choice == "tesoura" and computer_choice == "papel":
        print("Tesoura corta papel. Você ganhou!")
    elif user_choice == "pedra" and computer_choice == "Papel":
        print("Papel embrulha pedra. Você perdeu!")
    elif user_choice == "pedra" and computer_choice == "tesoura":
        print("Pedra quebra tesoura. Você ganhou!")


def clear():
    """clear screen command according OS type
    """
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')  


def main():
    """The main function
    """

    # game loop
    letsplay = "s"
    while letsplay.lower() != "n":

        # set computer choice
        computer_choice = computer_player_option()
    
        # set human player choice
        user_choice = user_choice_option()
       
        # show players choices
        game_choices(user_choice, computer_choice)

        # play game
        game_result(user_choice, computer_choice)

        # sign-out option
        letsplay = input("\nQuer jogar novamente? (s / n) ")

    # End game    
    print("\nFim de jogo. Até a próxima!\n")


## main program call
if __name__ == "__main__":
    main()