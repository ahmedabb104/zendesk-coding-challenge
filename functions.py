# The main menu options for the ticket viewer
def mainMenu():
    print("\nPlease enter a number for the following options:")
    print("1) View all tickets")
    print("2) View a single ticket")
    print("3) Exit")

# Parses ticket pages into readable lists of 25
def paginatedTickets(res, pageNum):
    ticketList = res.json()["tickets"]
    length = len(ticketList)
    lastTicket = pageNum * 25         # The last ticket number on the page
    firstTicket = (pageNum - 1) * 25  # The first ticket number on the page
    if lastTicket > length:
        lastTicket = length           # This is so we do not run into any index error
    for i in range(firstTicket, lastTicket):
        print(f"{ticketList[i]['id'] - 1}: '{ticketList[i]['subject']}' created at {ticketList[i]['created_at']} by {ticketList[i]['submitter_id']}")
    print("\nPress 1 to move to the previous page, 2 to move to the next page, or 3 to return to the menu")
    # ******* For testing purposes *******
    if pageNum < 1:
        return 0
    elif pageNum == 1 and firstTicket == 0 and lastTicket == 25:
        return 1
    elif pageNum == 2 and firstTicket == 25 and (lastTicket == 50 or lastTicket == len(ticketList)):
        return 1

# Takes in the response from the API, parsing all of the tickets into a readable list
def parseTickets(res):
    for ticket in res.json()["tickets"]:
        print(f"{ticket['id'] - 1}: '{ticket['subject']}' created at {ticket['created_at']} by {ticket['submitter_id']}")

# Gives individual ticket details
def individualTicket(res, ticketNum):
    ticket = res.json()["tickets"][int(ticketNum) - 1]
    print(f"\nTicket {ticket['id'] - 1}:\n  From: {ticket['submitter_id']}\n  On: {ticket['created_at']}\n  Subject: {ticket['subject']}\n  Message: {ticket['description']}\n")
    # ******* For testing purposes *******
    if int(ticketNum) < 1 or int(ticketNum) > len(res.json()["tickets"]):
        return 0
    else:
        return 1

# The main logic behind the program. Runs different code depending on the option picked. Will never take "3" as input, because of how it is implemented in main.py
def optionPicked(res, option):
    if option == "1":
        if len(res.json()["tickets"]) > 25:
            option1 = True  # Allows us to stay in the pagination state until the user exits
            pageNumber = 1
            while option1:
                paginatedTickets(res, pageNumber)
                nextorPrev = input()
                while (nextorPrev == "1" and pageNumber == 1) or (nextorPrev == "2" and pageNumber == -(len(res.json()["tickets"]) // -25)) or (nextorPrev not in "123"):
                    print("\nThat is invalid input. Please input another number")
                    nextorPrev = input()
                if (nextorPrev == "1"):
                    pageNumber -= 1  # Previous page
                elif (nextorPrev == "2"):
                    pageNumber += 1  # Next page
                else:
                    option1 = False  # Exits the pagination state
        else:
            parseTickets(res)  # If less than or equal to 25 tickets, we don't need pagination
    elif option == "2":
        print("Please enter the number of the ticket you wish to view")
        ticketNum = input()
        while int(ticketNum) < 1 or int(ticketNum) > len(res.json()["tickets"]):
            print("Please enter a valid ticket number.")
            ticketNum = input()
        individualTicket(res, ticketNum)
    else:
        print("Please enter a valid option")