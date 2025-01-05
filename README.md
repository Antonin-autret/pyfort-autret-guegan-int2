General presentation 

Projet title: FORT BOYARD SIMULATOR 
Contributors: Antonin AUTRET, Charles GUEGAN 

 

Description: In this project, we created an interactive game in Python based on the french “Fort boyard” tv show, we also built a simple interface for users to interact with the game. 

 

Key Features: Creation of a team of 1 to 3 players, multiple games such as mathematical, logical and chance challenges. You will also be able to try and solve the riddles of the famous Pere Fouras of Fort Boyard. All of which will allow you to acquire some keys and enter the treasure room. 

 

Technologies used: We used Python on PyCharm and GitHub to share our code.  

We used random and json libraries. 

 

Installation:   

 It is necessary to install all the files in the repository of the project. 

 

How to use: Open the project’s code in an IDE that supports Python run the main.py file and use the console to type the inputs. 

 

 
Technical documentation 

 

Game algorithm:  

1.The algorithm welcomes the user and explains the rules of the game. 

2.He then asks the user to create a team made up of 1 to 3 members. 

3.The game will do the following step until the players acquire 3 keys: 
3.1)The algorithm asks the player(s) to choose a type of challenge and the player who will participate, and the algorithm will randomly select a challenge among the given type. 
3.2) If the player wins the challenge, he acquires a key 

4.The players will enter the Tresure Room and will participate in the final challenge if they succede the algorithm will display a message  

 

Functions: 

Main.py:  

game(): fuction responsible for calling all the other function of the code in the right order according to game rules 

Utility functions: 

Key2(integer): takes an integer n as the argument and display a key drawing with ascii characters in the same lines n times 

Introduction(): display the introduction text that explain the rules to the players 

composeTeam()->list of dictionaries :a function that create a list of dictionaries where dictionaries represent the player’s information(name, profession, its role, the number of keys won) and ask the user to fill all the information .then it return the list 

challenges_menu()->integer: display all the challenges and ask the user to choose one then return the number corresponding to the choice of the user 

 

choose_player(list of dictionaries)->dictionary : this function takes as a parameter a list of dictionaries representing the team's information and display all the players information then it ask the player witch player will play the next challenge and return the corresponding number 

 

Math challeges: 

Factorial(integer)->integer: function that takes an integer as argument and return its factorial 

solve_linear_equation()->(integer,iteger,float):  function that generate two integer a and b between 1 and 10 and the solution of ax+b=0 

math_challenge_equation()->boolean : function that ask the solution af an equation to the player and return true if he's right and false if he's wrong 

math_challenge_factorial() ->boolean : function that generate a random integer between 1 and 10 and ask the user the factorial of it(return True if right and False otherwise) 

is_prime(integer) ->boolean: #takes a integer as argument and return true if it is prime and false if it is not 

 

nearest_prime(integer)->integer: find the nearest greater or equal prime number of n and return it 

math_challenge_prime()->boolean: ask the player to find the nearest prime number and return true if he's right and false if he's wrong 

math_challenge(): choose a random math challenge and call the coresponding function 

 

Chance challenges: 

 

shell_game()->boolean: challenge that ask the player to choose between three shells to find a key (in two tries) and return true if the player won and false if he loosed 

dice_game() ->boolean: challenge that ask the player to press enter to throw a dice reprensented by ascii char and return true if the player won and false if he loosed 

chance_challenge(): #choose a challenge from the logical one and execute the function 

 

Pere fouras challenge: 

load_file(string)->dictionary :load a json file and return what is inside 

pere_fouras_riddles()->boolean load riddles from the PFRiddles.json file and ask the user to solve it in less than three tries and return true if the player won and false if he loosed 

 
final_challenge: 

load_file(string)->dictionary :takes a string as the argument and return the content of the file with the argument as its name 
 

treasury_room()->boolean: load riddles from the TRClues.json file and ask the user to solve it in less than three tries and return true if the player won and false if he loosed 

 

 

Logical challenges: 

display_sticks (n):  integer -> none: This function display in the console the sticks left for the game of Nim 

-player _removal(n): integer -> integer: It returns the number of sticks removed by the player. 

-master_removal(n): integer -> integer. It applies an AI strategy based on the remainder of the division of n by 4. The AI (the game master) chooses the number of sticks to remove according to 

this strategy, with the goal of forcing the opponent to lose. It returns the number of 

sticks removed by the game master. 

-nim_game(): none -> boolean: This is the main function of the stick game. It will call the functions defined above to manage the flow of the game 

 

 

-display_grid(grid): 2D list -> none:  It displays the tictactoe grid 

-check_victory(grid, symbol): 2D list, character -> boolean: It examines the rows, columns, and diagonals of the grid to check if the symbol has won, returning True if it has, otherwise False. 

-master_move(grid, symbol): 2D list, character -> tuple: This function determines the game master's move first to win, then to block the player if necessary, and finally plays a random move if none of these actions is required. 

-player_turn(grid): 2D list -> none: It allows the player (symbol 'X') to place their symbol in an empty square. The grid is then updated with the player's move. 

-master_turn(grid): This function directly modifies the grid by placing the game master's move ('O'). The game master plays according to the strategy defined in the master_move() function.  

-full_grid(grid): 2D list -> boolean: It returns True if the grid is complete (no empty cells), otherwise False. This function is used to check whether the game has ended in a draw or can continue. 

-check_result(grid): 2D list -> boolean: It returns True if the game has ended, meaning that either player 'X' or the game master (player 'O') has won, or if the game has ended in a draw. It checks the results using the check_victory() and full_grid() functions. If no endof-game condition is met, it returns False, meaning that the game continues. 

-tictactoe_game(): none -> boolean: This is the main function that orchestrates the entire tictactoe game by calling all the functions used. It takes no parameters and returns True if player 'X' wins the game, and False otherwise 

 

 

Input and error management: 

if the player tries to input a number that is not allowed the game will loop until the number is in right interval. 

But we were not able to manage the error caused by a player inputting a word instead of a number because it is not in the right type 

 

Logbook

Project chronology: We did a large proportion of the project during the first 2 to 3 weeks of the given time for the intermediary submission (from the 28/11/2024 to the 19/12/2024). We ended the project during the last week of the final submission deadline (from the 30/12/2024 to the 05/01/2025) during which we completed the main, the utility functions, the final challenge, the tictactoe and provide the project the documentation. 



Task distribution:  

Antonin AUTRET worked on math challenges, the utility functions, the chance challenges, the Pere Fouras riddles, the program testing, the program commentaries, the excel, and the readme file. 

Charles GUEGAN worked on the logical challenges, the program testing, the commentaries, the excel and the readme file. 

 

Testing and Validation 

Test strategies: to test any function we just called it in the curent program during coding  and for the main game coding at the end we played the game multiple times just to se if the game was coherent and fun to play 