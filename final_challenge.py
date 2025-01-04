#load a json file and return its what is inside
import json
import random
def load_file(file):
    pf = open(file,"r")
    dico = json.load(pf)
    pf.close()
    return dico

def treasury_room():
    riddle =load_file('data/TRClues.json')["Fort Boyard"]
    list_years=list(riddle.keys())
    year =random.choice(list_years)
    nice =random.choice(list(riddle[year].values()))
    print("Well done adventurers, you have won 3 keys and can now take on the final challenge.\nThe challenge is as follows.\nYou have to guess a word using clues.To do this, you will have three attempts. Each time you try, another clue will be revealed.")
    for i in range(3):
        print(nice['Clues'][i])
    att = 3
    i=3
    while  att !=0:
        guess=input("Your guess:")
        if guess.lower() == nice["CODE-WORD"].lower():
            print("Correct! Congratulations, you have braved the trials of Fort Boyard and you each win 0 euros and the eternal respect of Passpartout.")
            return True
        elif att!=1:
            print("wrong.Try again, you have {} try left".format(att-1))
            print("new clue:",nice['Clues'][i])
            i+=1
        att -= 1
    print("sorry but you failed and are now stuck forever on the Fort Boyard with Olivier Minne as your only friend")
    return False
