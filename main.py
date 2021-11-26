from functions import *
from connect import response

# Main program loop
def mainLoop():
    quit = False
    option1 = False
    pageNumber = 1
    print("\n********** Welcome to the ticket viewer. **********")
    while not quit:
        mainMenu()
        option = input()
        if option == "1":
            if len(response.json()["tickets"]) > 25:
                option1 = True
                while option1:
                    paginatedTickets(pageNumber)
                    nextorPrev = input()
                    while (nextorPrev == "1" and pageNumber == 1) or (nextorPrev == "2" and pageNumber == -(len(response.json()["tickets"]) // -25)) or (nextorPrev not in "123"):
                        print("\nThat is invalid input. Please input another number")
                        nextorPrev = input()
                    if (nextorPrev == "1"):
                        pageNumber -= 1
                    elif (nextorPrev == "2"):
                        pageNumber += 1
                    else:
                        option1 = False
            else:
                parseTickets()
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

mainLoop()