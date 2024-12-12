import json
import random
#load a json file and return its what is inside
def load_file(file):
    pf = open(file,"r")
    dico = json.load(pf)
    pf.close()
    return dico

def pere_fouras_riddles():
    riddle =load_file('data/PFRiddles.json')[random.randint(0,11)]
    print(riddle['question'])
    a=input("the ")

pere_fouras_riddles()