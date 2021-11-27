import requests
from functions import *
from connect import response

# Main program loop
def mainLoop():
    quit = False  # Allows us to keep the program running until the user exits
    option1 = False
    pageNumber = 1
    print("\n********** Welcome to the ticket viewer. **********")
    while not quit:
        mainMenu()
        option = input()
        if option == "1":
            if len(response.json()["tickets"]) > 25:
                option1 = True  # Allows us to stay in the pagination state until the user exits
                while option1:
                    paginatedTickets(pageNumber)
                    nextorPrev = input()
                    while (nextorPrev == "1" and pageNumber == 1) or (nextorPrev == "2" and pageNumber == -(len(response.json()["tickets"]) // -25)) or (nextorPrev not in "123"):
                        print("\nThat is invalid input. Please input another number")
                        nextorPrev = input()
                    if (nextorPrev == "1"):
                        pageNumber -= 1  # Previous page
                    elif (nextorPrev == "2"):
                        pageNumber += 1  # Next page
                    else:
                        option1 = False  # Exits the pagination state
            else:
                parseTickets()  # If less than or equal to 25 tickets, we don't need pagination
        elif option == "2":
            print("Please enter the number of the ticket you wish to view")
            ticketNum = input()
            while int(ticketNum) < 1 or int(ticketNum) > len(response.json()["tickets"]):
                print("Please enter a valid ticket number.")
                ticketNum = input()
            individualTicket(ticketNum)
        elif option == "3":
            quit = True
        else:
            print("Please enter a valid option")

# Handling the API being unavailable, and running the program if it is available
try:
    response.raise_for_status()
    mainLoop()
except requests.exceptions.HTTPError:
    print('Sorry, the API is unavailable or you have entered the wrong authorization. Please try again.')