import random
from utility_functions import key2

def shell_game():
    l=["A","B","C"]
    print("There are three shells in front of you, A, B and C. Only one contain a key, to get it you have to guess under witch shell it is hidden. You have two tries")
    print("A  B  C")
    term='ies'
    pos_key = random.randint(0, 2)
    for i in range(2):
        print('you have {} tr{} left'.format(2-i,term))
        term='y'
        x=(input("choose a shell: ")).upper()
        if x==l[pos_key]:
            print('Congratulations! You found it')
            key2(1)
            return True
        else:
            print('The key is not in this shell')
    print('Sorry but the key was under the shell {}'.format(pos_key))
    return False

def dice_game():
    dice_p=[]
    dice_gm=[]
    die_face=(" -------\n|       |\n|   o   |\n|       |\n -------"," -------\n| o     |\n|       |\n|     o |\n -------"," -------\n| o     |\n|   o   |\n|     o |\n -------"," -------\n| o   o |\n|       |\n| o   o |\n -------"," -------\n| o   o |\n|   o   |\n| o   o |\n -------"," -------\n| o   o |\n| o   o |\n| o   o |\n -------")
    print("wellcome in this game you will face the game master in a dice game.\nIn your turn you will throw two dice, your goal is to have a six on one die,after you the game master will do the same thing\nthe first to do a six will win the key\nafter three turns the game will end in a draw.")
    for i in range(0,5,2):
        input("press enter too throw your dice\n")
        for j in range(2):
            dice_p.append(random.randint(0,5)) # goes from 0 to 5 because it is easier to search for the correct die face in the list
            dice_gm.append(random.randint(0, 5))
        print('{}\n{}'.format(die_face[dice_p[i]],die_face[dice_p[i+1]]))
        if dice_p[i]==5 or dice_p[i+1]==5:
            print('Congratulations! You win this key')
            key2(1)
            return True
        print("now it is the game master turn")
        input("press enter too see game master's throw\n")
        print('{}\n{}'.format(die_face[dice_gm[i]], die_face[dice_gm[i + 1]]))
        if dice_gm[i]==5 or dice_gm[i+1]==5:
            print('The game master won. No key for you')
            return False
    print('neither of you won. no one will have the key')
    return False
