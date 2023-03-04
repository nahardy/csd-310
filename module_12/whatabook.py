# Nick Hardy
# Assignment 12.3 WhataBook
# CYBR410-T302
# 03/04/2023

import sys
import mysql.connector
from mysql.connector import errorcode

 
# Database config object

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True

}
# Show the main menu 
def show_menu():
    print(" \n --Main menu-- ")
    print(" 1. View Locations\n  2. View books\n  3. User account\n 4. Exit ")
   
# User input for option
    try:
        choice = int(input(' Enter an option:'))
        return choice
    # Values not listed 
    except ValueError:
        print("\n That was not an option... :")
        sys.exit(0)

# Show location of whatabook
def show_locations(_cursor):
    
    _cursor.execute("SELECT store_id, locale FROM store")

    # Get the results 
    locations = _cursor.fetchall()

    # Display the results
    print(" --Store locations-- ")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

# Book query 
def show_books(_cursor):
    _cursor.execute ("SELECT book_id, book_name, author, details FROM book")

    #get the results
    books = _cursor.fetchall()

# Show the results
    print(" Books ")
    for book in books:
        print( "Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))

# Input user id 
def validate_user():
    try:
        user_id = int(input('\n Enter user ID: '))

        # Validate choice
        if user_id < 0 or user_id > 3:
            print("Invalid user id")
            sys.exit(0)
        return user_id
    
    # Close program upon error
    except ValueError:
        print("Invalid option")

        sys.exit(0)

# Displays user menu  #shows user account menu
def show_account_menu():
    try:
        print("\n -- Customer Menu --")
        print("1. View wishlist\n  2. Add book to wishlist\n  3. Return to main menu")
      
        account_option = int(input('Choose an option:'))
        return account_option

# Closes program if account option is invalid 
    except ValueError:
        print("Invalid option")
        sys.exit(0)
        
# Query for list of available books 
def show_wishlist(_cursor, user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    
    # Get the results
    wishlist = _cursor.fetchall()
   
    print("\n -- Showing your wishlist --  ")
    
 # Iterate over book in wishlist
    for book in wishlist:
        print("Book Name: {}\n Author:{}\n".format(book[4], book[5]))

# This shows books in the database that can be added to wishlist
def show_books_to_add(_cursor, user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    
    print(query)
                    # show results
    _cursor.execute(query)
    
    books_to_add = _cursor.fetchall()
    
    print("\n  -- Books that are available -- ")
 
 # Iterate over books
    for book in books_to_add:
        print("Book ID: {}\n Book Name:{}\n".format(book[0], book[1]))

# Insert book into wishlist
def add_book_to_wishlist(_cursor, user_id, book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))
    
try:
        # for handling errors w/ connecting to db
        
    db = mysql.connector.connect(**config)

        #for queries
    cursor = db.cursor()
    print("\n --Welcome to WhatABook-- ")

        #show main menu
    user_selection = show_menu()

        #while user selection is not 4 exit option
    while user_selection != 4:

            # Option 1 show locations
        if user_selection == 1:
            show_locations(cursor)
            

            # Option 2 show books
        elif user_selection == 2:
            show_books(cursor)

           # Validate user and show account menu
        elif user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()
            
               # While account option does not equal 3 exit option
            while account_option != 3:

                    # Call wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                    # Option 2 will show books to add not in their wishlist
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("Enter the id of the book you want to add:"))
                        
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                        # Commit changes
                    db.commit()            
                    print(" Book ID: {} was added to wishlist".format(book_id))
                    
                    # If selected option is less than 0 or greater than 3 display invalid input
                if account_option <0 or account_option >3:
                    print("Invalid input, try again")
                account_option = show_account_menu()
                        
# If selected option is less than 0 or greater than 4 display invalid input
        if user_selection < 0 or user_selection > 4:
            print(" Invalid input, try again")
            
        user_selection = show_menu()

    print("\n\n Program terminated...")

# Handles errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print( " The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else: 
        print(err)
finally:

    db.close