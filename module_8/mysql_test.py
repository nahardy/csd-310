#Nick Hardy Assignment 8.2 mysql_test.py
#Connection code used from step 3 of this assignment

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

    print("\n Database user {} connected to MySQL on host{}".format(config["user"], config["host"], config["database"]))

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