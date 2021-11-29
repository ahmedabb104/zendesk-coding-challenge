import unittest
import functions
from connect import response

class TestFunctions(unittest.TestCase):

    def test_paginatedTickets(self):
        edgeCase1 = functions.paginatedTickets(response, 0)
        edgeCase2 = functions.paginatedTickets(response, 1)
        case3 = functions.paginatedTickets(response, 2)
        self.assertEqual(edgeCase1, 0)
        self.assertEqual(edgeCase2, 1)
        self.assertEqual(case3, 1)

    def test_individualTicket(self):
        edgeCase1 = functions.individualTicket(response, 0)
        case2 = functions.individualTicket(response, -1)
        edgeCase3 = functions.individualTicket(response, 1)
        edgeCase4 = functions.individualTicket(response, len(response.json()["tickets"]))
        self.assertEqual(edgeCase1, 0)
        self.assertEqual(case2, 0)
        self.assertEqual(edgeCase3, 1)
        self.assertEqual(edgeCase4, 1)


# Allows us to run "python test_functions.py" in terminal
if __name__ == '__main__':
    unittest.main()