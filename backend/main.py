from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from model import Buku
#App object
app = FastAPI()

from database import(
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

from database import(
    fetch_one_buku,
    fetch_all_bukus,
    create_buku,
    update_buku,
    remove_buku,
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"ping":"pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")
    

@app.put("/api/todo{title}")
async def put_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request{title}") 


@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return " succesfully deleted todo item !"
    raise HTTPException(400, "Something went wrong / Bad Request{title}") 

    




@app.get("/api/buku")
async def get_buku():
    response = await fetch_all_bukus()
    return response

@app.get("/api/buku{judul}", response_model=Buku)
async def get_buku_by_judul(judul):
    response = await fetch_one_buku(judul)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.post("/api/buku", response_model=Buku)
async def post_buku(buku:Buku):
    response = await create_buku(buku.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")
    

@app.put("/api/buku{judul}")
async def put_buku(judul:str, harga:str):
    response = await update_buku(judul, harga)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request{judul}") 


@app.delete("/api/buku{judul}")
async def delete_buku(judul):
    response = await remove_buku(judul)
    if response:
        return " succesfully deleted todo item !"
    raise HTTPException(400, "Something went wrong / Bad Request{judul}") 

