import os
import time
import pyttsx3
import random

# Ensure these modules are installed: pyttsx3

''' Description:
    Caution!
    Use this code only for fun purposes.
    Do not modify it. avoid potential system crashes.
    This script contains loop values that could crash your system if tampered with.
'''

def tricky():
    # Possible numbers to add
    num = [10, 20, 30, 40, 50]

    # Choose a random number from the list
    random_number = random.choice(num)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Print and speak initial instructions
    print('''IN THIS GAME YOU HAVE ONLY 5 SECONDS TO THINK.
             BEFORE THE NEXT OUTPUT COMES.
             MAKE SURE YOU HAVE PEN PENCIL TO PLAY''')
    engine.say("IN THIS GAME YOU HAVE ONLY 10 SECONDS TO THINK BEFORE THE NEXT OUTPUT COMES. MAKE SURE YOU HAVE PEN PENCIL TO PLAY")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Print and speak instruction to think of a number
    print("Think of a number?")
    engine.say("Think of a number?")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Print and speak instruction to double the number
    print("Now double it.")
    engine.say("Now double it.")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Print and speak instruction to add a random number
    print(f"Now add {random_number} to it from my side.")
    engine.say(f"Now add {random_number} to it from my side.")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Print and speak instruction to divide by 2
    print("Now divide it by 2.")
    engine.say("Now divide it by 2.")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Print and speak instruction to subtract the original number
    print("Now subtract the number you initially thought of.")
    engine.say("Now subtract the number you initially thought of.")
    engine.runAndWait()

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("cls")

    # Determine and print the guessed number based on random_number
    if random_number == 10:
        print("5 is the answer in your mind!")
        engine.say("5 is the answer in your mind")
        engine.runAndWait()

    elif random_number == 20:
        print("10 is the answer in your mind")
        engine.say("10 is the answer in your mind")
        engine.runAndWait()

    elif random_number == 30:
        print("15 is the answer in your mind")
        engine.say("15 is the answer in your mind")
        engine.runAndWait()

    elif random_number == 40:
        print("20 is the answer in your mind")
        engine.say("20 is the answer in your mind")
        engine.runAndWait()

    elif random_number == 50:
        print("25 is the answer in your mind")
        engine.say("25 is the answer in your mind")
        engine.runAndWait()

if __name__ == "__main__":
    tricky()
