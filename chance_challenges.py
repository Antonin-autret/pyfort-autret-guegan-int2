import random

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
            return True
        else:
            print('The key is not in this shell')
    print('Sorry but the key was under the shell {}'.format(pos_key))
    return False

def dice_game():
    die_face=(" -------\n|       |\n|   o   |\n|       |\n -------"," -------\n| o     |\n|       |\n|     o |\n -------"," -------\n| o     |\n|   o   |\n|     o |\n -------"," -------\n| o   o |\n|       |\n| o   o |\n -------"," -------\n| o   o |\n|   o   |\n| o   o |\n -------"," -------\n| o   o |\n| o   o |\n| o   o |\n -------")
dice_game()