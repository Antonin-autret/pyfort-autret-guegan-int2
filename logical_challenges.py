from os import remove


def display_stick(n):
    for i in range(n):
        print("|",end="")
    print("")

def player_removal(n):
    r=0   #r is the number of stick removed by the player.
    if n>3:
        r = int(input("How many sticks do you want to remove (You can retrieve 1,2 or 3 sticks). "))
        while r!=1 and r!=2 and r!=3:
            print("Error : Invalid entry.")
            r = int(input("How many sticks do you want to remove (You can retrieve 1,2 or 3 sticks). "))
    elif n==3:
        r = int(input("How many sticks do you want to remove (You can retrieve 1 or 2 sticks). "))
        while r!=1 or r!=2:
            print("Error : Invalid entry.")
            r=int(input("How many sticks do you want to remove (You can retrieve 1 or 2 sticks). "))
    elif n==2:
        r = 1
        print("You can only retrieve 1 stick.")
    else:
        r=1
    return r

def master_removal(n):
    r=0     #r is the number of stick removed by the game master.
    if n%4==0:
        r=3
    elif n%4==3:
        r=2
    else:
        r=1
    if r==1:
        print("The game master removes 1 stick.")
    else:
        print("The game master removes "+str(r)+" sticks.")
    return r

def nim_game():
    n=20
    player_turn=True
    while n>0:
        display_stick(n)
        if player_turn:
            print("Player's turn.")
            n-=player_removal(n)
            player_turn=False
        else:
            n-=master_removal(n)
            player_turn=True
    if player_turn:
        print("The game master removed the last stick. The player wins !")
    else:
        print("The player removed the last stick. The player loses !")
    return player_turn

def next_player(n):
    if n==1:
        return 0
    else :
        return 1
def empty_grid():
    l=[['2',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return l
def display_grid(l, message):
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print('',l[i][j],'|',end='')
        print()
    print('-------------')
    print(message)
def ask_position():
    good = False
    while not(good) :
        good = True
        list = input().split(',')
        for val in list:
            if int(val)>3 or int(val)<1 or len(list)!=2:
                good =False
    return(int(list[0]),int(list[1]))
ask_position()

