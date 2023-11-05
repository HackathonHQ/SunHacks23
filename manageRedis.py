# import pip
# import os
# pip.main(['install', 'redis'])

import redis


import json
from dotenv import load_dotenv
import os
load_dotenv()


def createItem(itemName:str, itemDescription:str, itemPrice:float, itemImage:str):
    # code to create item in Redis
    r = redis.Redis(
        host='redis-10943.c60.us-west-1-2.ec2.cloud.redislabs.com',
        port=10943,
        password=os.getenv("REDIS_PASSWORD"),
        ssl_certfile="./redis_user.crt",
        ssl_keyfile="./redis_user_private.key",
        ssl_ca_certs="./redis_ca.pem",
    )
    
    newProduct = {
        "name": itemName,
        "descr": itemDescription,
        "price": itemPrice,
        "imgurl": itemImage
    }

    r.lpush("ProductsList", json.dumps(newProduct))

    return True


# def searchItem(itemName):
    

# createItem("item1", "item1 description", 1.99, "item1 image")
