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


math_challenge_factorial()

