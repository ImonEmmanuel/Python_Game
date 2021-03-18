"""
Coding Challenge 3, hangman.py
"""
# Coding Challenge 3, hangman.py
# Name: Eseka Precious
# Student No: 2024170


import time
import random
import os
import csv
import sys

os.system("clear")

inventory = []


def intro():
    print("You are lost in the woods.")
    print("You know that if you follow the right path, you will get to the nearest village.")
    time.sleep(1)
    print("You see that there are 2 paths ahead. In which one do you want to go(left or right)")
    enter_jungle()

print('WELCOME TO JUNGLE HUNT, I HOPE YOU WOULD ENJOY YOUR ADVENTURE')
"""         Difficulty Selection        """

def damage_effect(damage, val1, val2):
    spider_damage = random.randint(damage-5, damage)
    iron_dagger_damage = random.randint(val1, val2)
    player_damage = iron_dagger_damage
    return spider_damage, player_damage

def difficulty(level):
    if level in ['hard', 'h']:
        return damage_effect(damage=20, val1=5, val2=8)
    elif level in ['medium', 'm']:
        return damage_effect(damage=15, val1=8, val2=15)
    elif level in ['easy', 'e']:
        return damage_effect(damage=10, val1=15, val2=25)

def levels():
    print('Select the Level of expertise')
    xls = False
    xlist = []
    while not xls:
        diff = input().lower()
        if diff in ['easy', 'e', 'hard', 'h', 'medium', 'm']:
            spider_damage, player_damage = difficulty(level=diff)
            xlist.append(spider_damage)
            xlist.append(player_damage)
            xls = True
        else:
            print('Enter a correct level of Expertise')
    return xlist[0], xlist[1]

#++++++++++++++++++++

def intro_end():
    """
    Forest Entrance Function
    """
    print("Where do you want to go, left or right?")
    choice = input()
    if choice == "left":
        print("You go down the path to the left and...")
        time.sleep(1)
        print("You die a horrible death")
        print_game_over()
        sys.exit()

    elif choice == "right":
        print("You go down the path to the right and...")
        time.sleep(1)
        print("Notice that the trees are thinning out")
        time.sleep(1)

def choice1_end():
    """
    Forest Gems Function

    This function helps the player select an item immediately he enters the forest
    to serve as help/assistance to the player as he navigate/battle with enemies
    """
    print("You see a flash of light in the forest.")
    print("Do you want to risk the forest to go see what it was?(yes or no)")
    iron_dagger = input()
    if iron_dagger == "yes":
        print("You find an iron dagger!")
        inventory.append("iron dagger")
        print(inventory)
    elif iron_dagger == "no":
        print("You continue on")
    else:
        iron_dagger

def part_1():
    """
    Spider Like Function Built using symbols
    """
    print("You finally get out of the forest")
    time.sleep(1)
    print("You see a giant frost spider in the distance")
    print(r"""
               (
                )
               (
         /\  .-" "-.  /\
        //\\/  ,,,  \//\\
        |/\| ,;;;;;, |/\|
        //\\\;-" "-;///\\
       //  \/   .   \/  \\
      (| ,-_| \ | / |_-, |)
        //`__\.-.-./__`\\
       // /.-(() ())-.\ \\
      (\ |)   '---'   (| /)
       ` (|           |) `
         \)           (/)""")


def attack_or_run():
    """
    Attack or Run Function

    This function is implemeted and called when the player faces a challenge
    The player must decide what is best for him at this stages of the game play
    """
    choice2 = ""
    while choice2 != "1" and choice2 != "2":
        print("Do you want to attack it or run?(1 = attack, 2 = run)")
        choice2 = input()
    return choice2

def part_1_1(choice2):
    """
    Encounter Function 2
    """
    if choice2 == "2":
        print("You start to run away")
        time.sleep(1)
        print("You trip on a rock and...")
        time.sleep(1)
        safe = random.randint(1, 10)
        if safe == 1:
            print("You continue on towards the nearest village")
        else:
            print("You fall into a ravine and die")
            print_game_over()
            sys.exit()
    if choice2 == "1":
        if "iron dagger" in inventory:
            print("You run towards the spider with your iron dagger")
            time.sleep(1)
            print("You start to attack it and...")
            time.sleep(1)
        else:
            print("You desperatly try to kill the spider with your fists but fail miserably")
            print_game_over()
            sys.exit()

def encounter_1(choice2):
    """
    Encounter Function:

    This Function shoows/display how the Player and the Spider Health decreses
    when there both engage in a wrestle of power 
    """
    if choice2 == "1":
        john_smith_hp = 100
        giant_spider_hp = 80
        while True:
            giant_spider_hp = giant_spider_hp - player_damage
            john_smith_hp = john_smith_hp - spider_damage
            if giant_spider_hp < 1:
                print("You kill the spider")
                break
            print(f"Spider health: {giant_spider_hp}")
            time.sleep(0.5)

            if john_smith_hp < 1:
                print("You got killed by the spider")
                print_game_over()
                sys.exit()
            print(f"Your health: {john_smith_hp}")
            time.sleep(0.5)
        return john_smith_hp


def part_1_2(choice2):
    """
    Pick up Functions:

    This function is allows a player to pick up gems on the way
    """
    if choice2 == "1":
        bottle = ""
        while bottle != "yes" and bottle != "no":
            print("You find a strange bottle with some kind of potion in it.")
            print("Do you want to take it with you?")
            bottle = input()
    print("You spot a giant on the road")
    print_giant()
    time.sleep(1)
    if bottle == "yes":
        print("You know you cannot deafeat him, but perhaps the bottle could help you?")
        time.sleep(1)
        inventory.append("bottle")
    elif bottle == "no":
        print("You know you cannot deafeat him...")
        time.sleep(1)
        print("You try to run away but realize that it's hopeless as the giant closes in on you")
        time.sleep(1)
        print("Perhaps that bottle could have saved you...?")
        print_game_over()
        sys.exit()

    else:
        print("You know you cannot deafeat him...")
        time.sleep(1)
        print("You try to run away but realize that it's hopeless as the giant closes in on you.")
        print_game_over()
        sys.exit()

def part_1_3():
    """
    Inventory Function 
    """
    if "bottle" in inventory:
        choice3 = ""
        print("What do you want to do?")
        print("Print HELP if you don't know what to do")
        print("1.drink, 2.run, 3.fight, 4.apply to weapon")

        choice3 = input()
        if choice3 == "drink" or choice3 == "1":
            print("You drink the potion and collapse on the ground dead.")
            print("Maybe that wasn't such a good idea")
            print_game_over()
            sys.exit()

        elif choice3 in["fight", "run", "3", "2"]:
            print("You get destroyed by the giant")
            print_game_over()
            sys.exit()

        elif choice3 == "apply" or choice3 == "4":
            print("You apply the potion to your shortsword and charge the giant")
            time.sleep(1)
            print("You manage to cut the giant and he collapses to the ground.")
            time.sleep(1)
            print("You finally arrive to the village")

        else:
            part_1_3()
    
#### Leaderboard 
def leaderboard(score=None, username=None):
    """
    Leaderboard Function

    This Funcion uses Python inbuilt CSV Modules
    to create,read and update the leaderboard
    """
    if score and username != None:
        with open("leaderboard.csv", "a", newline='') as file:
            fields = ['score', 'name']
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow({'score' : score, 'name' : username})

        with open("leaderboard.csv", "r") as file:
            sortlist = []
            reader = csv.reader(file)
            for i in reader:
                sortlist.append(i)
        for ind, value in enumerate(sortlist):
            if ind != 0:
                value[0] = int(value[int(0)])

        for ind, value in enumerate(sortlist):
            print(value)


        for i in range(555):
            for i in range(len(sortlist)-1):
                if i != 0:
                    if sortlist[i][0] < sortlist[i+1][0]:
                        change = sortlist[i]
                        sortlist[i] = sortlist[i+1]
                        sortlist[i+1] = change
        for i in range(len(sortlist)-1):
            print(sortlist[i])
    else:
        print('Leaderboard has been Created Play/Win a session to create a new Leaderboard')

def play():
    """
    Play function to ask user if there would quit or still play
    """
    while True:
        user = input("Play Again? (Y/N) ").upper()
        if user == 'Y':
            main()
        else:
            print('Hope to see you again')
            sys.exit()

def main():
    """
    Main Game Driver FUnction
    """
    name = input('Enter your Name: ')
    playagain = "yes"
    if playagain == "yes":
        intro()
        intro_end()
        choice1_end()
        part_1()
        choice2 = attack_or_run()
        part_1_1(choice2)
        scorex = encounter_1(choice2)
        part_1_2(choice2)
        part_1_3()
        print('Do you want to view the Leader Board??: ')
        lb_input = input().lower()
        if lb_input == 'yes' or 'y':
            if str(scorex)[0] == '-':
                leaderboard(score=0, username=name)
            else:
                leaderboard(score=scorex, username=name)
            play()
        else:
            play()

def enter_jungle(): 
    """
    Jungle Function Built using symbols
    This is a Forest Entrace
    """
    print()
    print("   _________________________________________________________")
    print(r" /|     -_-                                             _-  |\ ")
    print(r"/ |_-_- _                                         -_- _-   -| \   ")
    print(r"  |                            _-  _--                      | ")
    print(r"  |                            ,                            |")
    print(r"  |      .-'````````'.        '(`        .-'```````'-.      |")
    print(r"  |    .` |           `.      `)'      .` |           `.    |          ")
    print(r"  |   /   |   ()        \      U      /   |    ()       \   |")
    print(r"  |  |    |    ;         | o   T   o |    |    ;         |  |")
    print(r"  |  |    |     ;        |  .  |  .  |    |    ;         |  |")
    print(r"  |  |    |     ;        |   . | .   |    |    ;         |  |")
    print(r"  |  |    |     ;        |    .|.    |    |    ;         |  |")
    print(r"  |  |    |____;_________|     |     |    |____;_________|  |  ")
    print(r"  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |")
    print(r"  |  |  / __  ()        -|        -  |  /  __--      -   |  |")
    print(r"  |  | /        __-- _   |   _- _ -  | /        __--_    |  |")
    print(r"  |__|/__________________|___________|/__________________|__|")
    print(r" /                                             _ -        lc \ ")
    print(r"/   -_- _ -             _- _---                       -_-  -_ \ ")
    print()

def print_giant():
    """
    Giant Function Built using symbols
    Will appear after passing the spider stage
    """
    print()
    print(r"                                                  ___I___ ")
    print(r"                                                 /=  |  #\ ")
    print(r"                                                /.__-| __ \ ")
    print(r"                                                |/ _\_/_ \| ")
    print(r"                                                (( __ \__)) ")
    print(r"                                             __ ((()))))()) __ ")
    print(r"                                           ,'  |()))))(((()|# `. ")
    print(r"                                          /    |^))()))))(^|   =\ ")
    print(r"                                         /    /^v^(())()()v^;'  .\ ")
    print(r"                                         |__.'^v^v^))))))^v^v`.__| ")
    print(r"                                        /_ ' \______(()_____(   | ")
    print(r"                                   _..-'   _//_____[xxx]_____\.-| ")
    print(r"                                  /,_#\.=-' /v^v^v^v^v^v^v^v^| _| ")
    print(r"                                  \)|)      v^v^v^v^v^v^v^v^v| _| ")
    print(r"                                   ||       :v^v^v^v^v^v`.-' |#  \, ")
    print(r"                                   ||       v^v^v^v`_/\__,--.|\_=_/ ")
    print(r"                                   ><       :v^v____|  \_____|_ ")
    print(r"                                ,  ||       v^      /  \       / ")
    print(r"                               //\_||_)\    `/_..-._\   )_...__\ ")
    print(r"                              ||   \/  #|     |_='_(     |  =_(_ ")
    print(r"                              ||  _/\_  |    /     =\    /  '  =\ ")
    print(r"                               \\\/ \/ )/ gnv |=____#|    '=....#| ")
    print()

def print_game_over():
    """
    Gameover Function Built using symbols
    This shows when you fail the mission
    """
    print()
    print("   _____          __  __ ______    ______      ________ _____  ")
    print(r"  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print(r" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
    print(r" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print(r" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print(r"  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\")
    print()

if __name__ == "__main__":
    spider_damage, player_damage = levels()
    iron_dagger_damage = player_damage
    main()