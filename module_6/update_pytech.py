#References: Krasso, P. (2020) (Lines 2, 4, 6, 8).  
from pymongo import MongoClient

url= "url= 'mongodb+srv://admin:admin@cluster0.aj9m1pr.mongodb.net/pytech'"

client = MongoClient(url= 'mongodb+srv://admin:admin@cluster0.aj9m1pr.mongodb.net/pytech')

db = client.pytech

#4 Call the find() method and output the documents to the terminal window.
find(students)

#5 Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name
#updating student id
_filter ={'student_id' : '1007'}

# last name to be updated
newvalues = { "$set": {'Last Name': Hardy}}

#update_one() method for single 
#updation.
collection.update_one(_filter, newvalues)

#printing the updated content of the database
cursor = collection.find()
for record in cursor:
    print(record)

#6 Call the find_one method by student_id 1007 and output the document to the terminal window. 

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


print("--DISPLAYING STUDENT DOCUMENT 1007 --")


print("End of program, press any key to continue....")