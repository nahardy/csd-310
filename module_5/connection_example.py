from pymongo import MongoClient
url= 'mongodb+srv://admin:admin@cluster0.aj9m1pr.mongodb.net/pytech'
client = MongoClient(url)


db = client.pytech

# example of inserting a new record into the student collection/table 
 db.students.insert_one({'student_id': "1007","first_name":"Nick", "last_name": "Hardy"})

def makeStudent(n):
    return {'first_name':"Fred"+n, "species": "human","home_planet": "earth-milky-way", "planet-age": "41billion"}

#db.students.insert_many([makeStudent(" 41b")])

#isDeleted = db.students.delete_one({"name": "Nick2"})
#print("""Deleted Nick: %(isDeleted)s""")

print("Number of student %s"%(db.students.count_documents({})))

print(db.list_collection_names())


# crud => create, read, update and delete

# message {
#     text, images,
#     user_id: "xx",
#     created_at: "sometime",
#     updated_at: "some time",
#     location: "gps cord",
# }