
from fastapi import FastAPI
import typing
from pymongo import MongoClient
import os

app = FastAPI()


@app.post("/insert_name")
def insert_name(name: str):
    #conectar al Mongo=mongodb://root:example@mongo:27017
    mongo_dir = 'mongodb://root:example@mongo:27017'
    client = MongoClient(mongo_dir)
    db = client['DB_API']
    col = db ['nombres']
    col.insert_one({'name': name})
    pass


@app.get("/names")
def names() -> typing.List[str]:
    return ["pepe", "maria"]










