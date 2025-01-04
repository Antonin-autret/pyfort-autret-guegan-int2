from chance_challenges import *
from utility_functions import *
from pere_fouras_challenge import *
from math_challenges import *

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
        #elif chall ==2:
        #    won =logical_challenge()
        elif chall ==3:
            won =chance_challenge()
        elif chall ==4:
            won =pere_fouras_riddles()
        if won:
            player['keys_wons']+=1

        keys=0
        for i in team:
            keys+=i['keys_wons']
    won_finalgame= treasury_room()
if __name__ == '__main__':
    game()