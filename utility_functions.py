def key2(n):
    line=["   @@@@%           ","  @     @@@@@@@@@@@","  @      @    @@ @ ","   @@@@%           "]
    for i in range(4):
        for j in range(n):
            print(line[i],end='')
        print('')
def Introduction():
    print("Welcome to the Fortress of Adventure! Only the bravest will conquer the challenges and claim the ultimate treasure. Are you ready to begin?")
    print("Your mission is simple:")
    print("Complete challenges to earn keys and unlock the treasure room.")
    print("Collect three keys to gain access to the treasure and claim your victory!")
def composeTeam():
    team =-1
    print("Now, tell me how many players are in your team? (the number of players cannot be greater than 3)")
    team = int(input())
    while team<1 or team >3:
        print("Please enter a number between 1 and 3")
        team = int(input())
    player1,player2,player3={},{},{}
    l=[player1,player2,player3]
    for i in range(team):
        l[i]["Name"]=input("what is your name player?")
        l[i]["profession"]=input("what is {}'s profession ?".format(l[i]["Name"]))
    leader=0
    if team!=1:
        leader=-1
        while leader<1 or leader >3:
            print("which one of the team member is the leader ? (enter the number of the player corresponding to the order in which you placed him in the team)")
            leader=int(input())
    else:
        leader=1
    for i in (l):
        i["role"]="member"
        i['keys_wons']=0
    l[leader-1]["role"]="leader"
    return l
def challenges_menu():
    print("chose your challenge\n1. Mathematics challenge\n2. Logic challenge\n3. Chance challenge\n4. Père Fouras' riddle")
    choose=-1
    while choose < 1 or choose > 4:
        int(input("please enter a number between 1 and 4"))
