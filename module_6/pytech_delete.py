#References: Krasso, P. (2020) (Lines 3, 6, 10, 13 in this code).  

# imports
from pymongo import MongoClient

# setup connection
url= 'mongodb+srv://admin:admin@cluster0.aj9m1pr.mongodb.net/pytech'
client = MongoClient(url)

# get db
db = client.pytech

#  get students collection
students = db.students

# utility function to print student information to console
def printStudent(stu):
     print(" Student ID: {} \n First Name: {}\n Last Name: {}\n\n".format(stu['student_id'],stu['first_name'],stu['last_name']))

#3 Call the find() method and display the results to the terminal window.
students_list = students.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for stu in students_list:
    printStudent(stu)


#4 Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
new_student_id = db.students.insert_one({'student_id': "1010","first_name":"Nick", "last_name": "Hardy"})
print("\n --INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id {}".format( new_student_id.inserted_id))

#5 Call the find_one() method and display the results to the terminal window.
studentFilter ={ 'student_id' : '1010'}
found_student = students.find_one(studentFilter)

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
printStudent(found_student)

# call the delete_one method to remove the student_test_doc
deleted_student =students.delete_one(studentFilter)
# print("deleted count: {}".format(deleted.deleted_count))

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for stu in students.find({}):
    printStudent(stu)

print("End of program, press any key to continue....")