import logging
import os
from typing import List

import database
import jsonschema
from bson.objectid import ObjectId
from dotenv import load_dotenv
from fastapi import Depends
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
logging.basicConfig(level=os.getenv("ZKAN_LOGGING_LEVEL", logging.INFO))

app = FastAPI()


class NewSchema(BaseModel):
    title: str
    body: dict


@app.on_event("startup")
async def connect_to_mongo():
    await database.connect(os.getenv("ZKAN_DB_URL", "mongodb://mongo/zkan"))
    db = await database.get_database()
    await db.get_collection("schemas").create_index("title", unique=True)


@app.on_event("shutdown")
async def close_mongo_connection():
    database.get_database().close()


@app.get("/ping")
async def ping():
    return dict(message="Hello World")


@app.get("/schemas", response_model=List[dict])
async def schemas(db=Depends(database.get_database)):
    schemas: List[dict] = []
    rows = db.get_collection("schemas").find()
    async for row in rows:
        schema = dict(id=str(row["_id"]), title=row["title"])
        schemas.append(schema)
    return schemas


@app.post("/schemas", response_model=dict)
async def schema_create(item: NewSchema, db=Depends(database.get_database)):
    try:
        jsonschema.Draft4Validator.check_schema(item.body)
    except Exception as e:
        print(e)
        raise e
    document = dict(title=item.title, body=item.body)
    result = await db.get_collection("schemas").insert_one(document)
    return dict(id=str(result.inserted_id))


@app.get("/schemas/{item_id}", response_model=dict)
async def schema(item_id: str, db=Depends(database.get_database)):
    row = await db.get_collection("schemas").find_one({"_id": ObjectId(item_id)})
    schema = dict(title=row["title"], body=row["body"])
    return schema


@app.delete("/schemas/{item_id}")
async def schema_delete(item_id: str, db=Depends(database.get_database)):
    await db.get_collection("schemas").delete_one({"_id": ObjectId(item_id)})
