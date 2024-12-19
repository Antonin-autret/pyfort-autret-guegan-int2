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
    att = 3
    while att>0:
        a=input("the ")
        if a.lower()== riddle['answer'].lower().split()[1]:
            return True
        else:
            att-=1
            print('try again you have {} attempts left'.format(att))
    return False

pere_fouras_riddles()