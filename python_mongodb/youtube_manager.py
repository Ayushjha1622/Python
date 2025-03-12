import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.hofa6.mongodb.net/ytmanager")

# Select the database
db = client["ytmanager"]

# List all collections in the database
collections = db.list_collection_names()

# Print the collections
print("Collections:", collections)
