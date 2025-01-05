import random
from utility_functions import key2

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
        print("The game master removed the last stick. The player wins the key!")
        key2(1)
    else:
        print("The player removed the last stick. The player loses !")
    return player_turn



def display_grid(grid):
    for row in grid:
        print(row[0], "|", row[1], "|",row[2])
        print("---------")

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

def master_turn(grid):
    print("Game master's turn.")
    move = master_move(grid, 'O')
    if move:
        (row,col) = move
        grid[row][col] = 'O'  # Place the master's symbol at the chosen position
    return grid

def full_grid(grid):
    for row in grid:
        if ' ' in row:
            return False
    return True

def check_result(grid):
    if check_victory(grid, 'X') or check_victory(grid, 'O'):
        return True
    if full_grid(grid):
        return True
    return False

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

def logical_challenge():
    n=random.randint(0,1)
    if n==0:
        return nim_game()
    else:
        return tictactoe_game()