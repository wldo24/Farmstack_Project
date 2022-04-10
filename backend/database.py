from model import Todo
from model import Buku
# MongoDB driver
import motor.motor_asyncio

async def get_server_info ():
    conn_str = "<mongodb://localhost:27017>"

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo
database2 = client.BukuList
collection2 = database2.buku


async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True


async def fetch_one_buku(judul):
    document = await collection2.find_one({"judul":judul})
    return document

async def fetch_all_bukus():
    bukus = []
    cursor = collection2.find({})
    async for document in cursor:
        bukus.append(Buku(**document))
    return bukus

async def create_buku(buku):
    document = buku
    result = await collection2.insert_one(document)
    return document

async def update_buku(judul, harga):
    await collection2.update_one({"title":title},{"$set":{"harga":harga}})
    document = await collection2.find_one({"judul":judul})
    return document

async def remove_buku(judul):
    await collection2.delete_one({"judul":judul})
    return True
