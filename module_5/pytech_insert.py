""" 
    Title: pytech_insert.py
    Author: Professor Krasso
    Date: 10 July 2020
    Description: Test program for inserting new documents 
                 into the students collection 
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
# url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"
url= 'mongodb+srv://admin:admin@cluster0.aj9m1pr.mongodb.net/pytech'


# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Thorin Oakenshield's data document 
thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
}

# Bilbo Baggins data document 
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
  }

# Frodo Baggins data document
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
   }

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
thorin_student_id = students.insert_one(thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")