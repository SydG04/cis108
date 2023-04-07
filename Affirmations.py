'''
Sydney Gilmore
Project 2
'''

def main():
    #import random library
    from random import randint


    #Quote outputs
    answer = input("Would you like to hear a inspiring/sentimental/funny quotes from Bojack Horseman, the Greatest Show of All Time? [y/n]").lower()
    while answer =='y':
            #Quote Number
            quote = randint(1,5)
            if quote == 1:
                print("'It gets easier. Everyday it gets a little easier. But you gotta do it everyday-that's the hard part. But it does get easier.' - A Jogger")
            elif quote == 2:
                print("'I'm responsible for my own happiness? I can't even be responsible for my own breakfast.' - Bojack")
            elif quote == 3:
                print("'Everybody deserves to be loved.' - Mr.Peanutbutter")
            elif quote == 4:
                print("'Nobody else gets to tell you what your story is.'- Ana")
            else:
                print("'You turn yourself around, that's what it's all about.' - Todd")
            answer = input("Would you like to hear another?: ").lower()
    print("Understandable, have a nice day.")

        

main()

'''
Pseudocode
1. Implement random library
2. Assign a quote a number
3. WRITE THE ACTUAL QUOTES
4. Create a loop that will run as many times as the user wants
5. When user says y, make it pick a different quote

Citations:
Bojack Horseman (Good show but season one is...:/)
Professor Jon
'''
