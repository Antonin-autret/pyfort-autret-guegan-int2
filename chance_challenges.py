#FORT BOYARD SIMULATOR, Antonin AUTRET and Charles GUEGAN
#This file contain all the funcion used for the chance challenges.


import random
from utility_functions import key2

def shell_game():
    l=["A","B","C"]
    print("There are three shells in front of you, A, B and C. Only one contain a key, to get it you have to guess under which shell it is hidden. You have two tries.")
    print("A  B  C")
    term='ies'
    pos_key = random.randint(0, 2)
    for i in range(2):
        print('You have {} tr{} left.'.format(2-i,term))
        term='y'
        x=(input("Choose a shell: ")).upper()
        if x==l[pos_key]:
            print('Congratulations! You found it.')
            key2(1)
            return True
        else:
            print('The key is not in this shell.')
    print('Sorry but the key was under the shell {}.'.format(pos_key))
    return False
#challenge that ask the player to choose between three shells to find a key (in two tries) and return true if the player won and false if he loosed
def dice_game():
    dice_p=[]
    dice_gm=[]
    die_face=(" -------\n|       |\n|   o   |\n|       |\n -------"," -------\n| o     |\n|       |\n|     o |\n -------"," -------\n| o     |\n|   o   |\n|     o |\n -------"," -------\n| o   o |\n|       |\n| o   o |\n -------"," -------\n| o   o |\n|   o   |\n| o   o |\n -------"," -------\n| o   o |\n| o   o |\n| o   o |\n -------")
    print("Welcome in this game you will face the game master in a dice game.\nIn your turn you will throw two dice, your goal is to have a six on one die,after you the game master will do the same thing\nthe first to do a six will win the key\nafter three turns the game will end in a draw.")
    for i in range(0,5,2):
        input("Press enter to throw your dice.\n")
        for j in range(2):
            dice_p.append(random.randint(0,5)) # goes from 0 to 5 because it is easier to search for the correct die face in the list
            dice_gm.append(random.randint(0, 5))
        print('{}\n{}'.format(die_face[dice_p[i]],die_face[dice_p[i+1]]))
        if dice_p[i]==5 or dice_p[i+1]==5:
            print('Congratulations! You win this key.')
            key2(1)
            return True
        print("Now it is the game master turn.")
        input("Press enter too see game master's throw.\n")
        print('{}\n{}'.format(die_face[dice_gm[i]], die_face[dice_gm[i + 1]]))
        if dice_gm[i]==5 or dice_gm[i+1]==5:
            print('The game master won. No key for you.')
            return False
    print('Neither of you won. No one will have the key.')
    return False
#challenge that ask the player to press enter to throw a dice reprensented by ascii char and return true if the player won and false if he loosed
def chance_challenge():
    n= random.randint(1,2)
    if n == 1:
        return dice_game()
    else:
        return shell_game()
#choose a challenge from the logical one and execute the function