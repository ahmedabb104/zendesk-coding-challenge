import requests
from dotenv import load_dotenv
import os

# Take environment variables from .env
load_dotenv()

# GET /api/v2/tickets using API token, storing it in response variable
url = "https://zccahmedabbas.zendesk.com/api/v2/tickets.json"
API_EMAIL = os.getenv("API_EMAIL")
API_TOKEN = os.getenv("API_TOKEN")
response = requests.get(url, auth=(API_EMAIL, API_TOKEN))

# The main menu options for the ticket viewer
def mainMenu():
    print("\nPlease enter a number for the following options:")
    print("1) View all tickets")
    print("2) View a single ticket")
    print("3) Exit")

# Parses the tickets into a readable list
def parseTickets():
    for ticket in response.json()["tickets"]:
        print(f"{ticket['id'] - 1}: '{ticket['subject']}' created at {ticket['created_at']} by {ticket['submitter_id']}")

# Gives individual ticket details
def individualTicket(ticketNum):
    ticket = response.json()["tickets"][int(ticketNum) - 1]
    print(f"Ticket {ticket['id'] - 1}:\n  From: {ticket['submitter_id']}\n  On: {ticket['created_at']}\n  Subject: {ticket['subject']}\n  Message: {ticket['description']}\n")

# Main program loop
def mainLoop():
    quit = False
    print("\n********** Welcome to the ticket viewer. **********\n")
    while not quit:
        mainMenu()
        option = input()
        if option == "1":
            parseTickets()
        elif option == "2":
            print("Please enter the number of the ticket you wish to view")
            ticketNum = input()
            individualTicket(ticketNum)
        elif option == "3":
            quit = True
        else:
            print("Please enter a valid option")

mainLoop()