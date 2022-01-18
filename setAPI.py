
# このファイルをWebページとして表示する際は、`uvicorn setAPI(ファイル名):app (--reload)'で表示可能 (--reloadはファイルの変更が反映されたら即時表示内容を変更する)`

from fastapi import FastAPI
from typing import Optional, List                  # Optionalでデータを任意化、ListでList型の型アノテーション可能
from pydantic import BaseModel, Field              # BaseModelを継承してデータ構造を定義、Fieldでインプットデータの制約条件付与

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shopInfo: ShopInfo
    items: List[Item]

app = FastAPI()

@app.post("/data/")
async def returnData(data:Data):
    return data

# /(ルートディレクトリ)にGETメソッドでリクエストが来た場合の処理を関数として定義
@app.get("/")
async def index():
    return {"message": "Hello"}

@app.get("/{name}")
async def info(name:str = "Tom", age:Optional[int] = None):     # nameはパスパラメータで入ってくる。ageはOptionalであり、クエリパラメータで入力された場合、入力が返ってくる
    return {"name": name, "age": age}