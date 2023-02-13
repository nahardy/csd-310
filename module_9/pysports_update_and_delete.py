# Nick Hardy Assignment 9.3 pysports_update_and_delete.py
#2/12/2023


#mysql import statement

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

# Inner join on player and team table
def team_players(locator, display_statement):
    
    locator.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = locator.fetchall()

    # shows insert, update, and delete display statements
    print("\n --{}--".format(display_statement))

    # iterate over the player data and display the results
    for player in players:

        print("Player ID: {}\n First Name:{}\n Last Name:{}\n Team Name: {}".format(player[0], player[1], player[2], player[3]))

try:
    database = mysql.connector.connect(**config)
# get the cursor named locator
    locator = database.cursor()

    # INSERT player query
    add_player = ("INSERT INTO player(first_name, last_name, team_id)""VALUES(%s, %s, %s)")

    # player data to be inserted
    player_info = ("Smeagol", "Shire Folk", 1)

    # inserting Smeagol in record
    locator.execute(add_player, player_info) 

    # committing insert
    database.commit()

    # showing all records in player table
    team_players(locator, "DISPLAYING PLAYERS AFTER INSERT")

    # UPDATE the new record that was inserted
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # show updated query
    locator.execute(update_player)

    # show all records in player table
    team_players(locator, "DISPLAYING PLAYERS AFTER UPDATE")

    # deleting Gollum 
    remove_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    locator.execute(remove_player)

    #show the records in the player table
    team_players(locator, "DISPLAYING PLAYERS AFTER DELETE")
    
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    
    if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

#This closes the connection to MySQL
finally:
    database.close()