#########################################
#Python Coding Exercise: Library Book Checkout System (created by ChatGPT - thanks AI!)
#########################################

#Objective
#Design a small system that processes a list of library book checkouts and returns a summary report.

#Input:
#A list of books currently available in the library.
#A list of checkout requests (each request includes a user, book title, and number of days requested).

books = [
    {"title": "1984", "copies": 4},
    {"title": "Brave New World", "copies": 2},
    {"title": "Fahrenheit 451", "copies": 3}
]
requests = [
    {"user": "Alice", "title": "1984", "days": 5},
    {"user": "Bob", "title": "1984", "days": 10},
    {"user": "Charlie", "title": "Brave New World", "days": 3},
    {"user": "Diana", "title": "The Hobbit", "days": 7}
]


#####################
# PART 1
# The following helper functions must be created first:
#####################

def is_valid_request(request):
    """
    Returns True if request contains 'user', 'title', and valid 'days' (>0).
    """

    # Write code here
   count = 0
    for book in request:
        if len(book) == 3 and book["days"] > 0:
            count += 1
    if count == len(request):
        return True



def find_book(books, title):
    """
    Returns the book dictionary matching the title, or None if not found.
    """
    
    for book in books:
        if book["title"] == title:
            return book
    return None


def is_available(book):
    """
    Returns True if at least one copy is available.
    """

    # Write code here


def checkout_book(book):
    """
    Decreases available copies by 1.
    """

    # Write code here

from datetime import datetime, timedelta

def calculate_due_date(days):
    """
    Returns a due date (string) based on today's date + given days.
    """

    # Write code here

#####################
# PART 2
# Now use the helper functions to create the main function:
#####################

def process_checkouts(books, requests):
    """
    Processes all checkout requests and returns a summary dictionary.
    """

    # Write code here
    
    return final_output

print(process_checkouts(books, requests))



"""
This function should:

1) Validate each request.
2) Check availability of the requested book.
3) Update inventory if checkout is successful.
4) Compute due dates.

Return a summary with:
Successful checkouts
Failed requests (with reasons)
Final inventory
"""

# The final output of the main function should have the form:
example_final_output = {
    "success": [
        {"user": "Alice", "title": "1984", "due_date": "2026-04-24"},
        ...
    ],
    "failed": [
        {"user": "Diana", "title": "The Hobbit", "days": 7, "reason": "Book not found"},
        ...
    ],
    "inventory": [
        {"title": "1984", "copies": 2},
        ...
    ]
}