'''
Sydney Gilmore
Project 3/Mid-Term
'''
#import randint 
from random import randint

def main():
    #candies range
    candies = [9,8,7,6,5,4,3,2,1,0]
    candy_bag = 1

#the game
    print("While trick or treating, you came across an old, run down shack. You thought about skipping it until you spotted a Ghostface statue sitting on a rock chair, holding a bucket full of candy.")
    print("Upon closer inspection, you noticed a sign on the bucket that read, 'Only take 1, or else  :)'")
    print("You decide to be a good kid and take just one. But, something inside you is telling you to take anoter..")

    for i in candies:
        choice = input("Do you wish to disobey the rules and take another? [y/n]: ").lower()
        #setting the chance of getting caught
        if choice == 'y':
            caught = randint(1,15) + i #I think I figured it out. Not sure
            if caught == 15:
                print("As your grubby fingers reached into the candy bin. The porch lights flicked on and the front door swung open. Before you can react, a large hand grabbed you by your collar and yanks you inside. You drop your candy bag and your",candy_bag,"pieces of candy. Maybe think twice before disobeying the rules :)")
                return
            #adding +1 to the candy bag
            candy_bag = candy_bag + 1
            print("You now have", candy_bag, "candies")
            #breaking when user gets all 10
            if candy_bag == 10:
                print("Congradulations! You have succfesully taken all 10 candies. Now the owners have to spend their hard earned money to buy more candy. I hope you're happy  :).")
                break
        elif choice == 'n':
            if candy_bag == 1:
                print("You decided to be a good kid and ignore your thoughts. You have successfully taken" ,candy_bag,"candy.")
            else:
                print("You have succesfully taken",candy_bag,"without getting caught.")
                print("As you're running away, you see the house lights flicker on and the front porch door open. But you already turned the corner before you can see what was behind that door.")
            break
main()
'''
Pseudocode:
1. Import random library
2. Create a variable for the candies in the bucket and the candy bag for the user. 
3. Implement loop to run a chance for as long as there is candy in the bowl. Have the candy bag increase by 1 each time the user says y.
4. Set a randint for the user to get caught.
5. Whether the user presses n or y or get caught, display how much candies they have/had
6. Once that's all figured out, make the chances of getting caught higher each time the loop runs
'''

