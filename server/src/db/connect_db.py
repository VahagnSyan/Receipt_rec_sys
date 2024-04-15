'''
Module for connecting to database
'''


from pymongo import MongoClient


def connect_db():
    '''
    Function for coneccting to database
    '''
    client = MongoClient("mongo-link")
    db = client["Cluster0"]
    collection = db["mycollection"]
    post = {"author": "ChatGPT", "text": "Hello MongoDB!"}
    collection.insert_one(post)
    result = collection.find_one({"author": "ChatGPT"})
    print(result)
