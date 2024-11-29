#file where all the function used for math challenges

import random



#function that takes an integer and return his factorial
def factorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
# function that generate a random integer between 1 and 10 and ask the user the factorial of it(return True if right and False otherwise)
def math_challenge_factorial():
    n=random.randint(1,10)
    print("Calculate the factorial of {}".format(n))
    ans=int(input("Your answer: "))
    if ans==factorial(n):
        print("Correct! You win a key.")
        return True
    else:
        print("Wrong! No key for you.")
        return False

# function that generate a linear equation and its solution
def solve_linear_equation():
    a=random.randint(1,10)
    b= random.randint(1, 10)
    return [a,b,-b/a]

# function that ask the solution af an equation to the player and return true if he's right and false if he's wrong
def math_challenge_equation():
    a=solve_linear_equation()[0]
    b=solve_linear_equation()[1]
    anw=solve_linear_equation()[2]
    print("Solve the equation {}x + {} = 0".format(a,b))
    x=float(input("What is the value of x: "))
    if x==anw:
        print("Correct! You win a key.")
        return True
    else:
        print("Wrong ! No key for you.")
        return False

