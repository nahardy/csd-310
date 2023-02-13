# Nick Hardy Assignment 9.2 pysports_join_queries.py
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

#Connection test code 

try:
    db = mysql.connector.connect(**config)

    cursor= db.cursor()

    # Inner Join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # return the results 

    players = cursor.fetchall()

    print("\n --DISPLAYING PLAYER RECORDS--")
    
    #iterate over the player data and display the results
    for player in players:

        print("Player ID: {}\n First Name:{} \n Last Name:{}\n Team Name: {}".format(player[0], player[1], player[2], player[3]))

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
    
    db.close()
