'''
Sydney Gilmore
Project 1: Dice
'''
import emoji
from random import randint
def main():
    #dice
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    dicetotal = dice1 + dice2

    #choices
    print("Is it over 7, 7, or under 7?")
    print ("Enter 1, if you think it's Over 7")
    print ("Enter 2, if you think it's 7")
    print ("Enter 3, if you think it's under 7")
    user_choice = int(input("Enter your choice:"))
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        user_choice = int(input("Bad user! Enter your choice:"))
    
    #selection
    if user_choice == 1: #over
        if dicetotal > 7:
            print("You win!","\N{party popper}")
        else:
            print ("You lose!","\N{broken heart}")
    elif user_choice == 2: #equal 7
        if dicetotal == 7:
            print("You win!","\N{party popper}")
        else:
            print ("You lose!","\N{broken heart}")
    elif user_choice == 3: #under
        if dicetotal < 7:
            print("You win!","\N{party popper}")
        else:
            print ("You lose!","\N{broken heart}")
          
main()
input()




'''
Pseudocode
1. Create two 6-sided die using random numbers and add the results
2. Input choice: over 7, 7, or under 7
3. If choice is over 7, check against dice total,
	If correct: you win, else: you lose
4. If choice is under 7, check against dice total,
	If correct: you win, else: you lose
5. If choice is 7, check against dice total,
	If correct: you win, else: you lose

Input 1: Win
Is it over 7, 7, or under 7?
Enter 1, if you think it's Over 7
Enter 2, if you think it's 7
Enter 3, if you think it's under 7
Enter your choice: 1

Output 1:
You win! (Party-popper-emoji)

Input 2: Lose
Is it over 7, 7, or under 7?
Enter 1, if you think it's Over 7
Enter 2, if you think it's 7
Enter 3, if you think it's under 7
Enter your choice: 3

Output 2:
You lose! (Heart-break-emoji)

Input 3: Invaild input
Is it over 7, 7, or under 7?
Enter 1, if you think it's Over 7
Enter 2, if you think it's 7
Enter 3, if you think it's under 7
Enter your choice: 20

Output 3:
Bad user! Enter your choice:

Citations:
Professor Jon (while statement)
https://stackoverflow.com/questions/70088987/display-user-choice-from-list (Make option Integers)
https://stackoverflow.com/questions/22022499/allow-user-to-choose-option-from-menu-with-for-loop (Print List of option)
https://codereview.stackexchange.com/questions/213627/forcing-the-user-to-choose-from-a-set-of-options-in-python (Helped with variable, user_choice)
'''
