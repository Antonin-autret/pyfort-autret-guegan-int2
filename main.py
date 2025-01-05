from utility_functions import *
from chance_challenges import *
from pere_fouras_challenge import *
from math_challenges import *
from logical_challenges import *
from final_challenge import *

def game():
    Introduction()
    team=composeTeam()
    keys=0
    while keys<3:
        chall =challenges_menu()
        player=choose_player(team)

        if chall==1:
            won =math_challenge()
        elif chall ==2:
            won =logical_challenge()
        elif chall ==3:
            won =chance_challenge()
        elif chall ==4:
            won =pere_fouras_riddles()
        if won:
            player['keys_wons']+=1

        keys=0
        for i in team:
            keys+=i['keys_wons']
#this function is responsible for playing the game according to the rules explained(creation of the team(1to3 players),playing challenges chosen by the players until they won 3 of them, and trying to win the final challenge)
#this function doesn't return anything because it is basically the main program
if __name__ == '__main__':
    game()