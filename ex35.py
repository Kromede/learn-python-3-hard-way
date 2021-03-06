from sys import exit

def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 500:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:                       # what does "while True" do?
        choice = input("> ")

        if choice == "take honey":
            deadd("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def monk_room():
    print("There is a Zen monk in a stone room.")
    print("He is sitting quietly, not moving.")
    print("Do you ask him something or leave him alone?")

    choice = input("> ")

    if "ask" in choice:
        print("The monk smacks you with a stick furiously yelling 'DIE! DIE! DIE!'")
        dead("You got beaten to death because you refused to give up.")
    elif "leave" in choice:
        start()
    else:
        print("The monk disciplines you and you become his apprentice.")
        print("After years of inquiry you get totally enilghtened.")
        print("There is no You anymore. \"You\" Win!")
        exit(0)

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right, left and in front.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "front":
        monk_room()
    else:
        dead("You stumble around the room until you starve.")


start()
