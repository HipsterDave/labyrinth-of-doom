import game
import text
import time
import sys
import os
import random
import saveload

typingspeed = 100

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def clear():
    os.system("cls")

def mainmenu():
    clear()
    text.title()
    typing("Welcome to the LABYRINTH OF DOOM! Would you like to PLAY, HELP, SEE CREDITS, or QUIT?\n")
    start = ""
    while start not in ["play", "help", "see credits", "quit"]:
        start = input("> ")
    if start == "play":
        clear()
        saveload.login_or_signup()
    elif start == "help":
        print("FILLER")
    elif start == "see credits":
        print("FILLER")
    elif start == "quit":
        print("FILLER")

def help():
    typing("THIS IS A FILLER")
    input("Please press enter to continue.")
    mainmenu()
