from connect import response

# The main menu options for the ticket viewer
def mainMenu():
    print("\nPlease enter a number for the following options:")
    print("1) View all tickets")
    print("2) View a single ticket")
    print("3) Exit")

# Parses ticket pages into readable lists of 25
def paginatedTickets(pageNum):
    ticketList = response.json()["tickets"]
    length = len(ticketList)
    lastTicket = pageNum * 25
    firstTicket = (pageNum - 1) * 25
    if lastTicket > length:
        lastTicket = length
    for i in range(firstTicket, lastTicket):
        print(f"{ticketList[i]['id'] - 1}: '{ticketList[i]['subject']}' created at {ticketList[i]['created_at']} by {ticketList[i]['submitter_id']}")
    print("\nPress 1 to move to the previous page, 2 to move to the next page, or 3 to return to the menu")

# Parses all of the tickets into a readable list
def parseTickets():
    for ticket in response.json()["tickets"]:
        print(f"{ticket['id'] - 1}: '{ticket['subject']}' created at {ticket['created_at']} by {ticket['submitter_id']}")

# Gives individual ticket details
def individualTicket(ticketNum):
    ticket = response.json()["tickets"][int(ticketNum) - 1]
    print(f"\nTicket {ticket['id'] - 1}:\n  From: {ticket['submitter_id']}\n  On: {ticket['created_at']}\n  Subject: {ticket['subject']}\n  Message: {ticket['description']}\n")