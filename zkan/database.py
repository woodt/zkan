import logging

from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    DB_NAME = "zkan"
    client: AsyncIOMotorClient = None

    def get_collection(self, collection: str):
        assert self.client
        return self.client[self.DB_NAME][collection]


db = Database()


async def connect(url):
    logging.info("Connecting to Mongo...")
    db.client = AsyncIOMotorClient(url)
    logging.info("Connected")


async def get_database() -> Database:
    return db
