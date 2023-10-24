from motor.motor_asyncio import AsyncIOMotorClient

from src.settings import DB_URI


class DataBase:

    def __init__(self, db_url: str):
        self.client = AsyncIOMotorClient(
            db_url,
            uuidRepresentation="standard",
        )

    def get_default_database(self):
        return self.client.get_default_database()

    def get_database(self, db_name: str):
        return self.client.get_database(db_name)


db = DataBase(DB_URI)
