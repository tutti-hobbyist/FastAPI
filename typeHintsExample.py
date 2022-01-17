from configparser import RawConfigParser
from typing import List, Dict

price:int = 100
tax:float = 1.1
list:List[int] = [i for i in range(5)]
dict:Dict[str, int] = {"ID_1": 1, "ID_2": 2}

def calcPrice(price:int, tax:float) -> float:
    return price*tax

if __name__ == "__main__":
    print(round(calcPrice(price, tax)))