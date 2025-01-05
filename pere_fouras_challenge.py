#FORT BOYARD SIMULATOR, Antonin AUTRET and Charles GUEGAN
#This file contains all the function used for the riddles of Père Fouras that will be told to the players.


import json
import random
from utility_functions import key2

def load_file(file):
    pf = open(file,"r")
    dico = json.load(pf)
    pf.close()
    return dico
#load a json file and return what is inside
def pere_fouras_riddles():
    riddle =load_file('data/PFRiddles.json')[random.randint(0,11)]
    print(riddle['question'])
    att = 3
    while att>0:
        a=input("the ")
        if a.lower()== riddle['answer'].lower().split()[1]:
            print("correct you win a key!")
            key2(1)
            return True
        else:
            att-=1
            if att==0:
                print("You lose!")
                return False
            print('try again you have {} attempts left'.format(att))
#load riddles from the PFRiddles.json file and ask the user to solve it in less than three tries and return true if the player won and false if he loosed
