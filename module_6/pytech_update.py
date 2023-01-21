
# Create a new directory under csd-310 and name it module_6.
# Inside the module_6 directory create a new file and name it pytech_update.py.
# Add the required Python code to connect to the students collection (refer to previous assignments for help).

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


# Call the find() method and output the documents to the terminal window.
print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
for stu in students.find({}):
    printStudent(stu)


studentQuery = {'student_id': '1007'}
# Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name.
update_student = students.update_one(studentQuery, {"$set":{'last_name':"Hardy"}})

# Call the find_one method by student_id 1007 and output the document to the terminal window.
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
printStudent(students.find_one(studentQuery))

print("End of program, press any key to continue....")