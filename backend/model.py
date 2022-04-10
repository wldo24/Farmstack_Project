from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    
class Buku(BaseModel):
    judul: str
    harga: str