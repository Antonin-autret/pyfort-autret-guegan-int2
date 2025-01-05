#FORT BOYARD SIMULATOR, Antonin AUTRET and Charles GUEGAN
#This file contains all the function used for the logical challenges.

import random
from utility_functions import key2

#Takes as parameter an integer n, representing the number of sticks remaining, and displays this number using bars (|), with each bar corresponding to one stick.
def display_stick(n):
    for i in range(n):
        print("|",end="")
    print("")

#Takes an integer n, representing the number of sticks remaining. This function asks the player to choose how many sticks to remove (1, 2, or 3), ensuring that
# the input is valid. It returns the number of sticks removed by the player.
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

#Takes as parameter an integer n, representing the number of sticks remaining. It applies an AI strategy based on the remainder of the division of n by 4.
# The AI (the game master) chooses the number of sticks to remove according to this strategy, with the goal of forcing the opponent to lose. It returns the number
# of sticks removed by the game master.
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

#This is the main function of the stick game. It will call the functions defined above to manage the flow of the game as follows:
#1. Initialize the number of sticks to 20.
#2. Uses a Boolean variable to indicate that it's the player's turn.
#3. As long as the number of sticks is not zero:
#Displays the remaining sticks.
#An iteration represents one turn, either that of the player or that of the game master.
#The number of sticks removed is retrieved by calling the corresponding function.
#Update and display the number of sticks remaining after each round.
#4. The game continues, alternating between players, until no sticks remain.
#5. The player who removes the last stick is declared the loser.
#6. The function returns True if the player wins, and False otherwise.
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
        print("The game master removed the last stick. The player wins the key!")
        key2(1)
    else:
        print("The player removed the last stick. The player loses !")
    return player_turn



#The function takes as parameter a 3x3 grid, represented by a 2D list, and displays it. Each grid cell can be empty (" ") or contain a symbol ('X' or 'O'), with a
#separator between lines.
def display_grid(grid):
    for row in grid:
        print(row[0], "|", row[1], "|",row[2])
        print("---------")

#This function takes a 2D grid list and a symbol string ('X' or 'O') as parameters. It examines the rows, columns, and diagonals of the grid to check if the symbol
#has won, returning True if it has, otherwise False.
def check_victory(grid, symbol):
    n = len(grid)

    # Check rows
    for row in grid:
        victory = True
        for cell in row:
            if cell != symbol:
                victory = False
                break
        if victory:
            return True

    # Check columns
    for col in range(n):
        victory = True
        for row in range(n):
            if grid[row][col] != symbol:
                victory = False
                break
        if victory:
            return True

    # Check diagonal
    victory = True
    for i in range(n):
        if grid[i][i] != symbol:
            victory = False
            break
    if victory:
        return True

    # Check anti-diagonal
    victory = True
    for i in range(n):
        if grid[i][n - 1 - i] != symbol:
            victory = False
            break
    if victory:
        return True
    else:
        return False

#The function takes as parameters a 2D grid list, representing the current state of the game grid, and a symbol string, representing the game master's symbol. This
#function determines the game master's move first to win, then to block the player if necessary, and finally plays a random move if none of these actions is
#required. It returns a tuple (row, column) corresponding to the coordinates of the chosen square.
def master_move(grid, symbol):
    n = len(grid)
    empty_cells = []
    player_symbol = 'X'
    if symbol == 'X':
        player_symbol = 'O'

    # Check if the master can win with the next move
    for row in range(n):
        for col in range(n):
            if grid[row][col] == ' ':  # Check if the cell is empty
                grid[row][col] = symbol  # Tentative move to see if the master win
                if check_victory(grid, symbol):
                    grid[row][col] = ' '  # Undo the tentative move
                    return (row, col)
                grid[row][col] = ' '  # Undo the tentative move

    # Check if the master needs to block the opponent's win
    for row in range(n):
        for col in range(n):
            if grid[row][col] == ' ':
                grid[row][col] = player_symbol  # Tentative move to see if the player can win
                if check_victory(grid, player_symbol):
                    grid[row][col] = ' '
                    return (row, col)
                grid[row][col] = ' '

    # Play a random move if there is no winning or blocking move
    for row in range(n):
        for col in range(n):
            if grid[row][col] == ' ':
                empty_cells.append((row,col))
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None   # If no moves are possible (so if the grid is full), return None

#This function takes a 2D grid list as a parameter, representing the current state of the game. It allows the player (symbol 'X') to place their symbol in an empty
#square. The player is prompted to enter the coordinates of the square in row, column format. Before placing the symbol, the function checks if the chosen square is
#empty. If the square is already occupied, the player is asked to select a different square. The grid is then updated with the player's move.
def player_turn(grid):
    print("Player X, it's your turn.")
    notValid = True
    while notValid:
        move = input("Enter your move in the form 'row,column': ")
        row, col = map(int, move.split(','))

        # Check if the entered coordinates are valid
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
            print("Invalid move : the coordinates are out of bounds. Try again.")

        else:
            # Check if the selected square is empty
            if grid[row][col] == ' ':
                grid[row][col] = 'X'
                notValid = False
            else:
                print("That square is already occupied. Choose a different square.")
    return grid

#The function takes as parameter a 2D grid list, representing the current state of the game grid. This function directly modifies the grid by placing the game
#master's move ('O'). The game master plays according to the strategy defined in the master_move() function.
def master_turn(grid):
    print("Game master's turn.")
    move = master_move(grid, 'O')
    if move:
        (row,col) = move
        grid[row][col] = 'O'  # Place the master's symbol at the chosen position
    return grid

#The function takes as parameter a 2D grid list, representing the current state of the game grid. It returns True if the grid is complete (no empty cells), otherwise
#False. This function is used to check whether the game has ended in a draw or can continue.
def full_grid(grid):
    for row in grid:
        if ' ' in row:
            return False
    return True

#This function takes a 2D grid list representing the current game state as a parameter. It returns True if the game has ended, meaning that either player 'X' or the
#game master (player 'O') has won, or if the game has ended in a draw. It checks the results using the check_victory() and full_grid() functions. If no end-of-game
#condition is met, it returns False, meaning that the game continues.
def check_result(grid):
    if check_victory(grid, 'X') or check_victory(grid, 'O'):
        return True
    if full_grid(grid):
        return True
    return False

#This is the main function that orchestrates the entire game. It takes no parameters and returns True if player 'X' wins the game, and False otherwise
#(i.e., if the game master wins or a draw occurs). Here's how it works:
#1. The grid (2D list) is initialized with empty spaces.
#2. A loop is defined to alternate turns between the player and the game master:
#   -The player_turn() function is called to manage the player's move. It allows
#   -the player to place their symbol ('X') on the grid.
#   -The check_result() function is called to check whether the game is over (win or draw). If player 'X' wins, the function returns True. If the game hasn’t ended
#after the player’s turn, the master_turn() function is called to allow the game master (symbol 'O') to make their move.
#   -The check_result() function is called again to check if the game master wins or if the grid is complete. If the game master wins or a draw is detected, the
#function returns False.
#3. The loop continues until a player wins or the grid is complete, indicating a draw. If either of these events occurs, the game ends
def tictactoe_game():
    grid = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    playerWin = False

    while check_result(grid) == False:
        display_grid(grid)
        player_turn(grid)
        if check_result(grid) == False:
            master_turn(grid)
    print("The game has ended.")
    display_grid(grid)
    if check_victory(grid, 'X'):
        playerWin = True
        print("The player X has won !")
        key2(1)
    return playerWin

#Randomly select a logical challenge.
def logical_challenge():
    n=random.randint(0,1)
    if n==0:
        return nim_game()
    else:
        return tictactoe_game()