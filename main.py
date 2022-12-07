from fastapi import FastAPI,Request,Depends

from pymongo import MongoClient

from routes.api import api_router

from routes.utility.login import get_current_active_user

import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
MONGODB_PORT = os.environ["MONGODB_PORT"]

app = FastAPI()

app.include_router(api_router, prefix="/routes")

@app.on_event("startup")
async def startup_db_client():
    # init connection to sql server
    ################################
    
    client = MongoClient(MONGODB_URL, int(MONGODB_PORT))
    app.mongodb_clinet = client
    # collection_name = "My_website"
    # db = client[collection_name]
    # db.users.insert_one(data)
    
@app.on_event("shutdown")
async def shutdown_db_client():
    pass

@app.get("/")
def root(current_user=Depends(get_current_active_user)):
    return {"message": "Hello World","current_user":current_user}

import time
@app.get("/test")
def root_test():
    time.sleep(2)
    return {"message_test": "Hello World_test"}

@app.get("/MongoClient")
def root_test_MongoClient():
    port = 27017
    mongodb_uri = "mongodb+srv://diamond:N8s8J6EF0xYjfla2@cluster0.i7nfk.mongodb.net/test"
    client = MongoClient(mongodb_uri, port)
    collection_name = "My_website"
    db = client[collection_name]
    # data = {"message_test": "Hello World_test"}
    username = "diamond"
    password = "2350"
    data = {"username": username
        ,"password":password
        ,"disabled":False
    }

    db.users.insert_one(data)
    return {"message_test": "Hello World_test"}

