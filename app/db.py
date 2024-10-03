import motor.motor_asyncio
from constant import MONGO_DB_NAME, MONGO_DB_URL, MONGO_DB_COLLECTION


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)
db = client[MONGO_DB_NAME]
collection = db[MONGO_DB_COLLECTION]

async def fetch_data():
    cursor = collection.find({}, {'embedding': 1, 'review_text': 1})
    data = []
    async for doc in cursor:
        data.append((doc['embedding'], doc['review_text']))
    return data