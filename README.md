# pyfort-autret-guegan-int2
1/ General presentation

Projet title: FORT BOYARD SIMULATOR 

Contributors: Antonin AUTRET, Charles GUEGAN

Description: In this project, we created an interactive game in Python based on the french “Fort boyard” tv show, we also built a simple interface for users to interact with the game.
 

Key Features: Creation of a team of 1 to 3 players, multiple games such as mathematical, logical and chance challenges. You will also be able to try and solve the riddles of the famous Pere Fouras of Fort Boyard. All of which will allow you to acquire some keys and enter the treasure room. 


Technologies used: We used Python on PyCharm and GitHub to share our code.
We used random and json libraries. 

Installation: It is necessary to install all the files in repository of the project. 

How to use: Open the project’s code in an IDE that support Python and use the console to type the inputs. 
 

2/Technical documentation

Game algorithm:
1. The algorithm welcomes the user and explains the rules of the game. 

2. He then asks the user to create a team made up of 1 to 3 members. 

3. The game will do the following step until the players acquire 3 keys: 

	3.1. The algorithm asks the player(s) to choose a type of challenge and the player who will participate, and the algorithm will randomly select a challenge among the given type. 

	3.2. If the player wins the challenge, he acquires a key 

4. Once the player(s) acquire 3 keys, he will be able to enter the treasure room and try to succeed in the final challenge of the Fort Boyard.


Functions:

Input and error management: 

if the player tries to input a number that is not allowed the game will loop until the number is in right interval. 

But we were not able to manage the error caused by a player inputing	 a word instead of a number because it is not in the right type 


 
3. Logbook

Project chronology :

Task distribution : 

 

4. Testing and Validation

Test strategies: 