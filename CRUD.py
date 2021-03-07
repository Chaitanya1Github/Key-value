'''
import pymongo

# create client
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") # protocol://IP Address:PORT/
print(f"Client: ", client)

# create Database/use database. if database with the name "Employee" exists then it`ll use the database otherwise new database with same name will be created.
mydb = client['Employee']
print(f"Database \"{mydb.name}\": ", mydb)


information = mydb.employeeinformation
print(f"Collection: ", information)


# record = {
#     "Name": "Chaitanya",
#     "Address": "Pune",
#     "Designation": "Software Engineeer",
# }
# information.insert_one(record)


# records = [
#     {
#         "Name": "Vishvadeep",
#         "Address": "Pune",
#         "Designation": "Software Engineeer",
#     },
#
#     {
#         "Name": "Rohit",
#         "Address": "Pune",
#         "Designation": "Software Engineeer",
#     },
# ]
# information.insert_many(records)
'''




from pymongo import MongoClient


# method1 (I prefer this method because we get different objects for client, database and collection. So we can access each of them separately)
client = MongoClient()                      # client created
my_database = client.my_database            # database created
my_collection = my_database.my_collection   # collection created


# method2
# my_collection = MongoClient().my_database.my_collection



######## Insert One Record ########
# record = {
#     "Name": "Chaitanya",
#     "Address": "Pune",
#     "Contact": "7447651902",
# }
# my_collection.insert_one(record)


######## Insert Many Records ########
# records = [
#     {
#         "Name": "Chaitanya",
#         "Address": "Pune",
#         "Designation": "Software Engineer"
#     },
#
#     {
#         "Name": "Vishvadeep",
#         "Address": "Pune",
#         "Contact": "7447651902",
#     },
#
#     {
#         "Name": "Rohit",
#     },
#
# ]
# inserted_data = my_collection.insert_many(records)
# print(inserted_data.Name)





###### Read first record #######
# first = my_collection.find_one()
# print(first)



###### Read all records #######
# documentList = my_collection.find()
# for document in documentList:
#     print(document)
#     print(document.get("Name"))



###### Read limited records #######
# documentList = my_collection.find().limit(5)
# for document in documentList:
#     print(document)
#     print(document.get("Name"))





########################################## Update #######################################

# 1. update_one(): used to update first occurrences of document

# find_values = {"Name": "Chaitanya"}                   # you can find values once you know how to use regex
# update_values = {"$set": {"Name": "chaitanya"}}
# my_collection.update_one(find_values, update_values)
# results = my_collection.find()
# for result in results:
#     print(result)


# 2.update_many(): used to update all the occurrences of the documents

# find_values = {"Address": "Pune"}                     # you can find values once you know how to use regex
# update_values = {"$set": {"Address": "Mumbai"}}
# my_collection.update_many(find_values, update_values)
# results = my_collection.find()
# for result in results:
#     print(result)







########################################## Delete #######################################

# 1. delete_one()

# find_values = {"Name": "Vishvadeep"}
# my_collection.delete_one(find_values)
# results = my_collection.find()
# for result in results:
#     print(result)


# 2. delete_many()

# find_values = {"Name": {"$regex": "^R"}}          # once you learn regex you can find complex values.
# deleted_documents = my_collection.delete_many(find_values)
# print(deleted_documents.deleted_count)
# results = my_collection.find()
# for result in results:
#     print(result)


# 3. delete all documents
# find_values = {}
# deleted_documents = my_collection.delete_many(find_values)
# print(deleted_documents.deleted_count)
# results = my_collection.find()
# for result in results:
#     print(result)




################################## drop collection ##################################
# my_collection.drop()


################################## drop database ##################################
client.drop_database('my_database')



########## this prints all the (fields)columns of each document #########
# documentList = my_collection.find()
# for document in documentList:
#     print(document)


########## this prints only (fields)columns marked with 1. #########
### if you specify one field 0, all the fields become 1 (except _id)
### if you specify one field 1, all the fields become 0 (except _id)
### you cannot use 0 and 1 at the same time (expect for _id)

# documentList = my_collection.find({}, {"Name": 1, "_id": 0})
# for document in documentList:
#     print(document)





############ Filter result (complex queries)#########
# my_query = {"Name": "Chaitanya", "Address": "Pune"}
# results = my_collection.find(my_query)
# for result in results:
#     print(result)

# my_query = {"Name": {"$gt": "R"}}       # Name start with greater than or equal to R
# results = my_collection.find(my_query)
# for result in results:
#     print(result)


######### Study regex in detail to filter data #########
# my_query = {"Name": {"$regex": "^V"}}    # name starts with letter V
# results = my_collection.find(my_query)
# for result in results:
#     print(result)




########### Sort ################

############ Ascending ##############
# results = my_collection.find().sort("Name")
# for result in results:
#     print(result)


############ Descending ##############
# results = my_collection.find().sort("Name", -1)
# for result in results:
#     print(result)



