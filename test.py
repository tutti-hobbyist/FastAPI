
# このファイルをWebページとして表示する際は、`uvicorn test:app (--reload)'で表示可能 (--reloadはファイルの変更が反映されたら即時表示内容を変更する)`

import imp
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

app = FastAPI()

# /(ルートディレクトリ)にGETメソッドでリクエストが来た場合の処理を関数として定義
@app.get("/")
async def index():
    return {"message": "Hello"}

@app.get("/{name}")
async def info(name:str = "Tom", age:Optional[int] = None):
    return {"name": name, "age": age}