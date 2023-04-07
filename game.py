'''
World of Zarcraft
'''

def main():
    #introduction
    print("Welcome hero to Zarcraft!")
    name = input("Enter your name: ")
    print("You must choose a class!")
    print("1. Human archer")
    print("2. Dark elf mage")
    print("3. Orc paladin")
    print()
    char_class = input("Make your choice: ")
    if char_class == '1':
        char_type = "Archer"
        char_race = "Human"
        char_health = 10
        char_str = 8
        char_int = 10
        char_dex = 12
    elif char_class == '2':
        char_type = "Mage"
        char_race = "Dark Elf"
        char_health = 10
        char_str = 10
        char_int = 12
        char_dex = 8
    else:
        char_type = "Paladin"
        char_race = "Orc"
        char_health = 10
        char_str = 12
        char_int = 8
        char_dex = 10
    print("Welcome "+name+", famed "+char_type)

    #tavern
    ale_check = True
    print("As you are traveling through a dark forest, you see a tavern ahead.")
    print("You enter the tavern")
    if ale_check == True:
        print("The crowd is raucous inside.Suddenly, a bottle is thrown at you.")
        if char_dex >= 10:
            print("You duck out of the way.")
        else:
            print("The bottle smacks you in the face... ouch")
            char_health -= 2
        ale_check = False
    print("The bartender yells out half-heartedly, '...Watch out'")
    choice = input("Whatllyahave?")
    if choice == "ale" or choice == "water" or choice == "wine":
        print("I'll bring out yer " + choice)
    else:
        print("Think yer funny, eh?")
        print("The bartender hits you wirh a battleaxe. Your adventure is over... [cue sad music]")
        return
        
    
    
main()

        
