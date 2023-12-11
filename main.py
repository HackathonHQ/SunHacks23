from fastapi import FastAPI

from manageRedis import ManageRedis


app = FastAPI()

mrs = ManageRedis()

@app.get("/searchItem/")
async def read_item(itemName: str = "Screwdriver"):
    return mrs.searchItem(itemName=itemName)

@app.get("/createItem/")
async def read_item(itemName: str = "Screwdriver", itemDescription: str = "A screwdriver", itemPrice: float = 1.99, itemImage: str = "https://www.homedepot.com/p/DEWALT-8-in-1-Ratcheting-Screwdriver-DWHT69233/206510455"):
    return mrs.createItem(itemName=itemName, itemDescription=itemDescription, itemPrice=itemPrice, itemImage=itemImage)

