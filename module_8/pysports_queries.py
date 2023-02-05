#Nick Hardy 
#Assignment 8.3 pysports_queries
#02/05/2023

#mysql import statement used from assignment 8.2

import mysql.connector
from mysql.connector import errorcode

# database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


#Connection test code 
try:

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # this will display the results of teams 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for the team/player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # grabs results from the cursor object then prints
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    
    for player in players:   # This displays the results of players
        
        print("Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Press any key to continue... ")

# Error statement to catch errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

#This closes the connection to MySQL
finally: #This closes the connection to MySQL
     db.close()

