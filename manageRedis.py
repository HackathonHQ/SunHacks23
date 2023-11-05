# import pip
# import os
# pip.main(['install', 'scikit-learn'])

import redis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
    
    # newProduct = {
    #     "name": itemName,
    #     "descr": itemDescription,
    #     "price": itemPrice,
    #     "imgurl": itemImage
    # }

    r.lpush("NamesList", itemName)
    r.lpush("DescrList", itemDescription)
    r.lpush("PriceList", itemPrice)
    r.lpush("ImgUrlList", itemImage)

    return True


def searchItem(itemName):
    r = redis.Redis(
        host='redis-10943.c60.us-west-1-2.ec2.cloud.redislabs.com',
        port=10943,
        password=os.getenv("REDIS_PASSWORD"),
        ssl_certfile="./redis_user.crt",
        ssl_keyfile="./redis_user_private.key",
        ssl_ca_certs="./redis_ca.pem",
    )
    if(r.lpos("NamesList", itemName, count=0) != None):
        return r.lpos("NamesList", itemName, count=0)
    elif(r.lpos("DescrList", itemName, count=0) != None):
        return r.lpos("DescrList", itemName, count=0)
    else:
        return None    


with open("newItem.txt", "r") as f:
    itemName, itemDescription, itemPrice, itemImage = f.read().splitlines()

createItem(itemName, itemDescription, float(itemPrice), itemImage)

