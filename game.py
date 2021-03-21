import time
import os
import sys
import random
import functions
import text
import saveload
import items

typingspeed = 100

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def tutorial():
    clear()
    saveload.save()
    typing("Welcome to the LABYRINTH OF DOOM, where nothing is weird.\n")
    typing("You will go around the labyrinth, fighting monsters and getting loot.\n")
    typing("Before we start, what is your name?\n")
    name = input("> ")
    saveload.data.name = name
    saveload.save()
    typing("Well hello there, " + saveload.data.name + "!\n")
    typing("Now that we know your name, we need to choose your class. This will influence your starting armor and tools.\n")
    text.classes()
    classes = ""
    while classes not in ["1", "2", "3", "4"]:
        classes = input("> ")
    if classes == "1":
        clear()
        saveload.data.Class = "Tank"
        saveload.data.armor = items.iron_armor
        saveload.data.secondary = items.wooden_shield
        typing("You have chosen the TANK class!\n")
        saveload.save()
    if classes == "2":
        clear()
        saveload.data.Class = "Warrior"
        saveload.data.armor = items.leather_cap
        saveload.data.primary = items.stone_sword
        typing("You have chosen the WARRIOR class!\n")
        saveload.save()
    if classes == "3":
        clear()
        saveload.data.Class = "Moneybags"
        saveload.data.coins = 50
        typing("You have chosen the MONEYBAGS class!\n")
        saveload.save()
    if classes == "4":
        clear()
        saveload.data.Class = "Engineer"
        saveload.data.secondary = items.explosives
        typing("You have chose the ENGINEER class!\n")
        saveload.save()
    typing("Before we begin, do you want to look at your inventory? (y/n)\n")
    y_n1 = ""
    if y_n1 not in ["y", "n"]:
        y_n1 = input("> ")
    if y_n1 == "y":
        clear()
        typing("Ok! Here is your inventory!\n")
        time.sleep(1)
        inventory()
        input("Please press enter to continue.")
        level_1()
    elif y_n1 == "n":
        clear()
        typing("Let's start with our game.\n")
        level_1()

def inventory():
    clear()
    print(saveload.data.name + "'s Inventory:")
    print("Class : " + saveload.data.Class)
    print("Armor : " + saveload.data.armor.name)
    print("Primary Item : " + saveload.data.primary.name)
    print("Secondary Item : " + saveload.data.secondary.name)
    print("Coins : " + str(saveload.data.coins))

def welcome_back():
    clear()
    typing("Welcome back, " + saveload.data.name + "!\n")
    typing("I see that you are on level " + str(saveload.data.savepoint) + ".\n")
    typing("Well, let's teleport you there!\n")
    time.sleep(2)
    if saveload.data.savepoint == 1:
        level_1()

def level_1():
    typing("LEVEL 1 BEGINNING!\n")
    time.sleep(2)
    clear()
    text.pic1()
    print("+-------------------------------------+")
    typing("As you walk around the first level, you see that there is a locked door, a pathway to the right, and a pathway to the left.\n")
    typing("However, there are 3 keys on a table in front of you.\n")
    typing("There is also a sign on a table. It reads:\n")
    typing("Here are three keys upon this table. One of them will open the door. If you choose that wrong key, you die.\n")
    typing("Also, here is a good thing to know. We change the key that goes to the door each time you attempt this level.\n")
    keys = [1, 2, 3]
    random_key = random.choice(keys)
    text.keychoice()
    option1 = ""
    while option1 not in ["1", "2", "3", "4", "5"]:
        option1 = input("> ")
    if option1 == "1":
        clear()
        typing("You took the left pathway.\n")
        typing("Since you took the pathway, you need to do a very hard activity.\n")
        typing("Pick a door. If you pick the wrong door, you lose. If you pick the right door, you win!\n")
        text.door()
        door = ""
        while door not in ["1", "2", "3"]:
            door = input("> ")
        if door == "1":
            typing("You open door 1.\n")
            typing("You opened the wrong door.\n")
            text.you_lost()
            input("Please press enter to continue.\n")
            welcome_back()
        elif door == "2":
            typing("You open door 2.\n")
            typing("Yay! You opened the correct door!\n")
            typing("Time for the BOSS ROUND.\n")
            typing("You will be given a random number between 1 and 10.\n")
            typing("That number will be added on to your damage level of your weapon.\n")
            typing("Your damage level is " + str(saveload.data.primary.damage) + ".\n")
            typing("You will need to damage the boss on a certain number.\n")
            typing("Also, different bosses will fight you with different strengths.\n")
            typing("Time to meet the boss!\n")
            time.sleep(2)
            boss1 = ["Sludge Monster", "Teddy Bear of Doom", "King Bat"]
            random_boss1 = random.choice(boss1)
            typing("The boss is the: " + random_boss1 + ".\n")
            typing("The BOSS FIGHT is beginning!\n")
            time.sleep(2)
            if random_boss1 == "Sludge Monster":
                clear()
                text.sludge_monster()
            elif random_boss1 == "Teddy Bear of Doom":
                clear()
                text.teddybear()
            elif random_boss1 == "King Bat":
                clear()
                text.bat_king()
            print("+-------------------------------------+")
            numbers_monster = [5, 6, 7]
            random_monster_number = random.choice(numbers_monster)
            typing("Your monster will have a strength of " + str(random_monster_number) + ".\n")
            typing("Your strength level is...\n")
            numbers_player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            random_number_player1 = random.choice(numbers_player1)
            time.sleep(1)
            typing(str(random_number_player1) + "!\n")
            added_damage_level = random_number_player1 + saveload.data.primary.damage
            typing("Added with your damage level, you attack the monster with a damage level of " + str(added_damage_level) + ".\n")
            if added_damage_level >= random_monster_number:
                typing("Yay! You beat the monster!\n")
                typing("The monster has been destroyed.\n")
                typing("You have made it out of the labyrinth! For now...\n")
                text.to_be_continued()
                exit()
            else:
                typing("You lost the battle...\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
        elif door == "3":
            typing("You open door 3.\n")
            typing("You opened the wrong door.\n")
            text.you_lost()
            input("Please press enter to continue.\n")
            welcome_back()
    elif option1 == "2":
        clear()
        typing("You took the right pathway.\n")
        typing("Since you took the pathway, you need to do a very hard activity.\n")
        typing("Pick a door. If you pick the wrong door, you lose. If you pick the right door, you win!\n")
        text.door()
        door = ""
        while door not in ["1", "2", "3"]:
            door = input("> ")
        if door == "1":
            typing("You open door 1.\n")
            typing("You opened the wrong door.\n")
            text.you_lost()
            input("Please press enter to continue.\n")
            welcome_back()
        elif door == "2":
            typing("You open door 2.\n")
            typing("You opened the wrong door.\n")
            text.you_lost()
            input("Please press enter to continue.\n")
            welcome_back()
        elif door == "3":
            typing("You open door 3.\n")
            typing("Yay! You opened the correct door!\n")
            typing("Time for the BOSS ROUND.\n")
            typing("You will be given a random number between 1 and 10.\n")
            typing("That number will be added on to your damage level of your weapon.\n")
            typing("Your damage level is " + str(saveload.data.primary.damage) + ".\n")
            typing("You will need to damage the boss on a certain number.\n")
            typing("Also, different bosses will fight you with different strengths.\n")
            typing("Time to meet the boss!\n")
            time.sleep(2)
            boss1 = ["Sludge Monster", "Teddy Bear of Doom", "King Bat"]
            random_boss1 = random.choice(boss1)
            typing("The boss is the: " + random_boss1 + ".\n")
            typing("The BOSS FIGHT is beginning!\n")
            time.sleep(2)
            if random_boss1 == "Sludge Monster":
                clear()
                text.sludge_monster()
            elif random_boss1 == "Teddy Bear of Doom":
                clear()
                text.teddybear()
            elif random_boss1 == "King Bat":
                clear()
                text.bat_king()
            print("+-------------------------------------+")
            numbers_monster = [5, 6, 7]
            random_monster_number = random.choice(numbers_monster)
            typing("Your monster will have a strength of " + str(random_monster_number) + ".\n")
            typing("Your strength level is...\n")
            numbers_player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            random_number_player1 = random.choice(numbers_player1)
            time.sleep(1)
            typing(str(random_number_player1) + "!\n")
            added_damage_level = numbers_player1 + saveload.data.primary.damage
            typing("Added with your damage level, you attack the monster with a damage level of " + str(added_damage_level) + ".\n")
            if added_damage_level >= random_monster_number:
                typing("Yay! You beat the monster!\n")
                typing("The monster has been destroyed.\n")
                typing("You have made it out of the labyrinth! For now...\n")
                text.to_be_continued()
                exit()
            else:
                typing("You lost the battle...\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
    elif option1 == "3":
        clear()
        text.pic2()
        print("+-------------------------------------+")
        typing("You picked the first key.\n")
        if random_key == 1:
            typing("Hooray! The first key was the correct option!\n")
            typing("You unlock the locked door.\n")
            typing("When the door opens, you find your first enemy.\n")
            typing("They are mutant bats!\n")
            typing("You must fight them to get to the second door.\n")
            text.bat_choice()
            bat_choice = ""
            while bat_choice not in ["1", "2", "3"]:
                bat_choice = input("> ")
            if bat_choice == "1":
                clear()
                text.pic3()
                print("+-------------------------------------+")
                typing("You attempt to fight the bats.\n")
                typing("However, the mutant bats fly up...\n")
                typing("And drop their radioactive bat guano on you!\n")
                typing("This turns you into fertilizer.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
            elif bat_choice == "2":
                clear()
                text.pic4()
                print("+-------------------------------------+")
                typing("You attempt to befriend the bats, by giving them a gift.\n")
                typing("You might not know this, but the bats LOVE gifts!\n")
                typing("Because you befriended them, they let you through.\n")
                typing("Time for the BOSS ROUND.\n")
                typing("You will be given a random number between 1 and 10.\n")
                typing("That number will be added on to your damage level of your weapon.\n")
                typing("Your damage level is " + str(saveload.data.primary.damage) + ".\n")
                typing("You will need to damage the boss on a certain number.\n")
                typing("Also, different bosses will fight you with different strengths.\n")
                typing("Time to meet the boss!\n")
                time.sleep(2)
                boss1 = ["Sludge Monster", "Teddy Bear of Doom", "King Bat"]
                random_boss1 = random.choice(boss1)
                typing("The boss is the: " + random_boss1 + ".\n")
                typing("The BOSS FIGHT is beginning!\n")
                time.sleep(2)
                if random_boss1 == "Sludge Monster":
                    clear()
                    text.sludge_monster()
                elif random_boss1 == "Teddy Bear of Doom":
                    clear()
                    text.teddybear()
                elif random_boss1 == "King Bat":
                    clear()
                    text.bat_king()
                print("+-------------------------------------+")
                numbers_monster = [5, 6, 7]
                random_monster_number = random.choice(numbers_monster)
                typing("Your monster will have a strength of " + str(random_monster_number) + ".\n")
                typing("Your strength level is...\n")
                numbers_player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                random_number_player1 = random.choice(numbers_player1)
                time.sleep(1)
                typing(str(random_number_player1) + "!\n")
                added_damage_level = random_number_player1 + saveload.data.primary.damage
                typing("Added with your damage level, you attack the monster with a damage level of " + str(added_damage_level) + ".\n")
                if added_damage_level >= random_monster_number:
                    typing("Yay! You beat the monster!\n")
                    typing("The monster has been destroyed.\n")
                    typing("You have made it out of the labyrinth! For now...\n")
                    text.to_be_continued()
                    exit()
                else:
                    typing("You lost the battle...\n")
                    text.you_lost()
                    input("Please press enter to continue.")
                    welcome_back()

            elif bat_choice == "3":
                clear()
                text.pic5()
                print("+-------------------------------------+")
                typing("You attempt to trick the bats into letting you through the area.\n")
                typing("You tell the bats that there is an emergency in a different room.\n")
                typing("They don't belive you.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
        else:
            typing("The first key was not the correct one. :(\n")
            text.you_lost()
            input("Please press enter to continue.")
            welcome_back()
    elif option1 == "4":
        clear()
        text.pic2()
        print("+-------------------------------------+")
        typing("You picked the second key.\n")
        if random_key == 2:
            typing("Hooray! The second key was the correct option!\n")
            typing("You unlock the locked door.\n")
            typing("When the door opens, you find your first enemy.\n")
            typing("They are mutant bats!\n")
            typing("You must fight them to get to the second door.\n")
            text.bat_choice()
            bat_choice = ""
            while bat_choice not in ["1", "2", "3"]:
                bat_choice = input("> ")
            if bat_choice == "1":
                clear()
                text.pic3()
                print("+-------------------------------------+")
                typing("You attempt to fight the bats.\n")
                typing("However, the mutant bats fly up...\n")
                typing("And drop their radioactive bat guano on you!\n")
                typing("This turns you into fertilizer.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
            elif bat_choice == "2":
                clear()
                text.pic4()
                print("+-------------------------------------+")
                typing("You attempt to befriend the bats, by giving them a gift.\n")
                typing("You might not know this, but the bats LOVE gifts!\n")
                typing("Because you befriended them, they let you through.\n")
                typing("Time for the BOSS ROUND.\n")
                typing("You will be given a random number between 1 and 10.\n")
                typing("That number will be added on to your damage level of your weapon.\n")
                typing("Your damage level is " + str(saveload.data.primary.damage) + ".\n")
                typing("You will need to damage the boss on a certain number.\n")
                typing("Also, different bosses will fight you with different strengths.\n")
                typing("Time to meet the boss!\n")
                time.sleep(2)
                boss1 = ["Sludge Monster", "Teddy Bear of Doom", "King Bat"]
                random_boss1 = random.choice(boss1)
                typing("The boss is the: " + random_boss1 + ".\n")
                typing("The BOSS FIGHT is beginning!\n")
                time.sleep(2)
                if random_boss1 == "Sludge Monster":
                    clear()
                    text.sludge_monster()
                elif random_boss1 == "Teddy Bear of Doom":
                    clear()
                    text.teddybear()
                elif random_boss1 == "King Bat":
                    clear()
                    text.bat_king()
                print("+-------------------------------------+")
                numbers_monster = [5, 6, 7]
                random_monster_number = random.choice(numbers_monster)
                typing("Your monster will have a strength of " + str(random_monster_number) + ".\n")
                typing("Your strength level is...\n")
                numbers_player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                random_number_player1 = random.choice(numbers_player1)
                time.sleep(1)
                typing(str(random_number_player1) + "!\n")
                added_damage_level = random_number_player1 + saveload.data.primary.damage
                typing("Added with your damage level, you attack the monster with a damage level of " + str(added_damage_level) + ".\n")
                if added_damage_level >= random_monster_number:
                    typing("Yay! You beat the monster!\n")
                    typing("The monster has been destroyed.\n")
                    typing("You have made it out of the labyrinth! For now...\n")
                    text.to_be_continued()
                    exit()
                else:
                    typing("You lost the battle...\n")
                    text.you_lost()
                    input("Please press enter to continue.")
                    welcome_back()

            elif bat_choice == "3":
                clear()
                text.pic5()
                print("+-------------------------------------+")
                typing("You attempt to trick the bats into letting you through the area.\n")
                typing("You tell the bats that there is an emergency in a different room.\n")
                typing("They don't belive you.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
        else:
            typing("The second key was not the correct one. :(\n")
            text.you_lost()
            input("Please press enter to continue.")
            welcome_back()
    elif option1 == "5":
        clear()
        text.pic2()
        print("+-------------------------------------+")
        typing("You picked the third key.\n")
        if random_key == 3:
            typing("Hooray! The third key was the correct option!\n")
            typing("You unlock the locked door.\n")
            typing("When the door opens, you find your first enemy.\n")
            typing("They are mutant bats!\n")
            typing("You must fight them to get to the second door.\n")
            text.bat_choice()
            bat_choice = ""
            while bat_choice not in ["1", "2", "3"]:
                bat_choice = input("> ")
            if bat_choice == "1":
                clear()
                text.pic3()
                print("+-------------------------------------+")
                typing("You attempt to fight the bats.\n")
                typing("However, the mutant bats fly up...\n")
                typing("And drop their radioactive bat guano on you!\n")
                typing("This turns you into fertilizer.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
            elif bat_choice == "2":
                clear()
                text.pic4()
                print("+-------------------------------------+")
                typing("You attempt to befriend the bats, by giving them a gift.\n")
                typing("You might not know this, but the bats LOVE gifts!\n")
                typing("Because you befriended them, they let you through.\n")
                typing("Time for the BOSS ROUND.\n")
                typing("You will be given a random number between 1 and 10.\n")
                typing("That number will be added on to your damage level of your weapon.\n")
                typing("Your damage level is " + str(saveload.data.primary.damage) + ".\n")
                typing("You will need to damage the boss on a certain number.\n")
                typing("Also, different bosses will fight you with different strengths.\n")
                typing("Time to meet the boss!\n")
                time.sleep(2)
                boss1 = ["Sludge Monster", "Teddy Bear of Doom", "King Bat"]
                random_boss1 = random.choice(boss1)
                typing("The boss is the: " + random_boss1 + ".\n")
                typing("The BOSS FIGHT is beginning!\n")
                time.sleep(2)
                if random_boss1 == "Sludge Monster":
                    clear()
                    text.sludge_monster()
                elif random_boss1 == "Teddy Bear of Doom":
                    clear()
                    text.teddybear()
                elif random_boss1 == "King Bat":
                    clear()
                    text.bat_king()
                print("+-------------------------------------+")
                numbers_monster = [5, 6, 7]
                random_monster_number = random.choice(numbers_monster)
                typing("Your monster will have a strength of " + str(random_monster_number) + ".\n")
                typing("Your strength level is...\n")
                numbers_player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                random_number_player1 = random.choice(numbers_player1)
                time.sleep(1)
                typing(str(random_number_player1) + "!\n")
                added_damage_level = random_number_player1 + saveload.data.primary.damage
                typing("Added with your damage level, you attack the monster with a damage level of " + str(added_damage_level) + ".\n")
                if added_damage_level >= random_monster_number:
                    typing("Yay! You beat the monster!\n")
                    typing("The monster has been destroyed.\n")
                    typing("You have made it out of the labyrinth! For now...\n")
                    text.to_be_continued()
                    exit()
                else:
                    typing("You lost the battle...\n")
                    text.you_lost()
                    input("Please press enter to continue.")
                    welcome_back()

            elif bat_choice == "3":
                clear()
                text.pic5()
                print("+-------------------------------------+")
                typing("You attempt to trick the bats into letting you through the area.\n")
                typing("You tell the bats that there is an emergency in a different room.\n")
                typing("They don't belive you.\n")
                text.you_lost()
                input("Please press enter to continue.")
                welcome_back()
        else:
            typing("The third key was not the correct one. :(\n")
            text.you_lost()
            input("Please press enter to continue.")
            welcome_back()