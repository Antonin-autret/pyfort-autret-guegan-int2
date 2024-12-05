import json
#load a json file and return its what is inside
def load_file(file):
    pf = open(file,"r")
    dico = json.load(pf)
    pf.close()
    return dico
