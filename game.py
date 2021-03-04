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
    os.system("cls")

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
        typing("Ok! Here is your inventory:\n")
    elif y_n1 == "n":
        clear()
        typing("Let's start with our game.\n")

def inventory():
    print(saveload.data.name + "'s Inventory:")