import time 
import random

name = input("Write your name plases!")
time.sleep(2)

print("welcome, " + name + ". One moment to take look!!")
time.sleep(2)

def print_action(getBack_to_print):
    print(getBack_to_print)

def intro(item, option):
    print_action( name + " You find yourself standing in an open field, filled " "with grass and yellow wildflowers.")
    time.sleep(2)

    print_action("Rumor has it that a " + option + " is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    
    print_action("In front of you is a house.")
    time.sleep(2)
    
    print_action("To your right hand is a dark cave.")
    time.sleep(2)
    
    print_action("In your left hand you hold your trusty (but not very effective) dagger.")
    time.sleep(2)

def house(item, option):
    print_action("You approach the door of the house.")
    time.sleep(2)
    
    print_action("You are about to knock when the door opens and out steps a " + option + ".")
    time.sleep(2)
    
    print_action("Eep! This is the " + option + "'s house!")
    time.sleep(2)
    
    print_action("The " + option + " attacks you!")
    time.sleep(2)
    
    if "sword" not in item:
        print_action("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        time.sleep(2)

    while True:
        choice = input("Would you like to (1) fight, or (2) to run away?")
        if choice == "1":
            if "sword" in item:
                
                print_action("As the " + option + " moves to attack, you unsheathe your new sword.")
                time.sleep(2)
                
                print_action("The Sword of Agoroth shines brightly in your hand as you prepare yourself for the attack.")
                time.sleep(2)
                
                print_action("But the" + option + "takes one look at your shiny new toy and runs away!")
                time.sleep(2)
                
                print_action("You have rid the town of the" + option + "." "You are victorious!")
                time.sleep(2)
            
            else:
                print_action("You do your best...")
                time.sleep(2)

                print_action("but your dagger is no match for the " + option + ".")
                time.sleep(2)

                print_action("You have been defeated!")
                time.sleep(2)

            play_again()
            break

        if choice == "2":
            print_action("You run back into the field. Luckily, you don't seem to have been followed.")
            time.sleep(2)

            field(item, option)
            break

def cave(item, option):
    if "sword" in item:
        print_action("You peer cautiously into the cave.")
        time.sleep(2)

        print_action("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        time.sleep(2)

        print_action("You walk back to the field.")
        time.sleep(2)

    else:
        print_action("You peer cautiously into the cave.")
        time.sleep(2)

        print_action("It turns out to be only a very small cave.")
        time.sleep(2)

        print_action("Your eye catches a glint of metal behind a rock.")
        time.sleep(2)

        print_action("You have found the magical Sword of Agoroth!")
        time.sleep(2)

        print_action("You discard your silly old dagger and take the sword with you.")
        time.sleep(2)

        print_action("You walk back out to the field.")
        time.sleep(2)

        item.append("sword")
    field(item, option)

def field(item, option):
    
    print_action("Enter 1 to knock on the door of the house.")
    time.sleep(2)

    print_action("Enter 2 to peer into the cave.")
    time.sleep(2)

    print_action("What would you like to do " + name + "?")
    time.sleep(2)

    while True:
        choice = input("(Please choice 1 or 2.)")
        if choice == "1":
            house(item, option)
            break
        elif choice == "2":
            cave(item, option)
            break

time.sleep(2)

def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    
    if again == "y":
        print_action("Excellent! Restarting this game ...")
        time.sleep(2)
        
        play_game()

    elif again == "n":
        print_action("Thanks for playing! See you later.")
        time.sleep(2)
    
    else:
        play_again()

time.sleep(2)

def play_game():
    item = []
    option = random.choice([ "pirate", "dragon", "Lion",
    "gorgon" ])
    intro(item, option)
    field(item, option)

play_game()