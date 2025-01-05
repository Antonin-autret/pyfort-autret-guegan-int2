#FORT BOYARD SIMULATOR, Antonin AUTRET and Charles GUEGAN
#This file contains all the utility functions that are used for creating a team and the convenience of the game. It also containq additional features.

def key2(n):
    line=["   @@@@%           ","  @     @@@@@@@@@@@","  @      @    @@ @ ","   @@@@%           "]
    for i in range(4):
        for j in range(n):
            print(line[i],end='')
        print('')
# takes an integer n as the argument and display a key drawing with ascii characters in the same lines n times
def Introduction():
    print("Welcome to the Fortress of Adventure! Only the bravest will conquer the challenges and claim the ultimate treasure. Are you ready to begin?")
    print("Your mission is simple:")
    print("Complete challenges to earn keys and unlock the treasure room.")
    print("Collect three keys to gain access to the treasure and claim your victory!")
#diplay the introduction text that explain the rules to the players
def composeTeam():
    team =-1
    print("Now, tell me how many players are in your team? (the number of players cannot be greater than 3)")
    team = int(input())
    while team<1 or team >3:
        print("Please enter a number between 1 and 3")
        team = int(input())
    l=[]
    for i in range(team):
        l.append({})
    for i in range(team):
        l[i]["Name"]=input("What is your name, player?:")
        l[i]["profession"]=input("What is {}'s profession ?".format(l[i]["Name"]))
    leader=0
    if team!=1:
        leader=-1
        while leader<1 or leader >team:
            print("which one of the team member is the leader ? (enter the number of the player corresponding to the order in which you placed him in the team)")
            leader=int(input())
    else:
        leader=1
    for i in (l):
        i["role"]="member"
        i['keys_wons']=0
    l[leader-1]["role"]="leader"
    return l
# a function that create a list of dictionaries where dictionaries represent the players information(name,profession,its role,the number of keys won) and ask the user to fill all the informations.then it return the list
def challenges_menu():
    print("chose your challenge\n1. Mathematics challenge\n2. Logic challenge\n3. Chance challenge\n4. Père Fouras' riddle")
    choose=-1
    while choose < 1 or choose > 4:
        choose =int(input("please enter a number between 1 and 4:"))
    return choose
#display all the challenges and ask the user to choose one then return the number corresponding to the choice of the user
def choose_player(team):
    for i in team:
        print("({}) -{}".format(i["profession"],i["role"]))
    chosenplayer=-1
    while chosenplayer>len(team) or chosenplayer<1:
        print("Enter the player who is going to play the challenge:",end='')
        chosenplayer =int(input())
    return team[chosenplayer-1]
#this function takes as a parameter a list of dictionaries representing the team's information and display all the players information then it ask the player witch player will play the next challenge and return the corresponding number