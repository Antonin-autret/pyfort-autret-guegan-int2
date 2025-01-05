#file where all the function used for math challenges

import random
from utility_functions import key2



def factorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
#function that takes an integer and return his factorial
def math_challenge_factorial():
    n=random.randint(1,10)
    print("Calculate the factorial of {}".format(n))
    ans=int(input("Your answer: "))
    if ans==factorial(n):
        print("Correct! You win a key.")
        key2(1)
        return True
    else:
        print("Wrong! No key for you.")
        return False
# function that generate a random integer between 1 and 10 and ask the user the factorial of it(return True if right and False otherwise)

def solve_linear_equation():
    a=random.randint(1,10)
    b= random.randint(1, 10)
    return [a,b,-b/a]
# function that generate a linear equation and its solution

def math_challenge_equation():
    a=solve_linear_equation()[0]
    b=solve_linear_equation()[1]
    anw=solve_linear_equation()[2]
    print("Solve the equation {}x + {} = 0".format(a,b))
    x=float(input("What is the value of x: "))
    if x==anw:
        print("Correct! You win a key.")
        key2(1)
        return True
    else:
        print("Wrong ! No key for you.")
        return False
# function that ask the solution af an equation to the player and return true if he's right and false if he's wrong

def is_prime(n):
    cpt=0
    for i in range(1,n+1):
        if n%i==0:
            cpt+=1
    if cpt==2:
        return True
    else:
        return False
#return true if n is prime and false if it is not


def nearest_prime(n):
    found=False
    while not found:
        if is_prime(n):
            return n
        else:
            n+=1
#find the nearest greater or equal prime number of n

def math_challenge_prime():
    n=random.randint(10,20)
    print("find the nearest prime number above {}".format(n))
    x=int(input("Your answer: "))
    if nearest_prime(n)==x:
        print("Correct! You win a key.")
        key2(1)
        return True
    else:
        print("Wrong ! No key for you.")
        return False
#ask the player to find the nearest prime number and return true if he's right and false if he's wrong
def math_challenge():
    n=random.randint(1,3)
    if n==1:
        return math_challenge_prime()
    elif n==2:
        return math_challenge_factorial()
    else:
        return math_challenge_equation()
