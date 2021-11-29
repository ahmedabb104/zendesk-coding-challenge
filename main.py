import requests
from functions import *
from connect import response

# Main program loop
def mainLoop():
    quit = False  # Allows us to keep the program running until the user exits
    print("\n********** Welcome to the ticket viewer. **********")
    while not quit:
        mainMenu()
        option = input()
        if option != "3":
            optionPicked(response, option)
        else:
            quit = True

# Handling the API being unavailable, and running the program if it is available
try:
    response.raise_for_status()
    mainLoop()
except requests.exceptions.HTTPError:
    print('Sorry, the API is unavailable or you have entered the wrong authorization. Please try again.')
