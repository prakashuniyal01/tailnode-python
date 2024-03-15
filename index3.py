

# ----------------- index3.py -------------_#

from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017/")


db = client.test_database

collection = db.test_collection


post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

posts = db.collection
post_id = posts.insert_one(post).inserted_id
post_id


cyberkingsid@gmail.com