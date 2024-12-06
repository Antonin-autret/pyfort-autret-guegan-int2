def display_stick(n):
    for i in range(n):
        print("|",end="")
def player_removal(n):
    m=0
    while(n>0):
        if n>3:
            while m!=1 and m!=2 and m!=3:
                m=int(input("How many sticks do you want to remove"))
        elif n==2:
            while m!=1 and m!=2:
                m=int(input("How many sticks do you want to remove"))
        elif n==1:
            while m!=1:
                m=int(input("How many sticks do you want to remove (1,"))

def master_removal(n):


def nim_game(n):