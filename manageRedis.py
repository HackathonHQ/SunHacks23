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

class ManageRedis:
   def __init__(self):
      self.r = redis.Redis(
         host='redis-10943.c60.us-west-1-2.ec2.cloud.redislabs.com',
         port=10943,
         password=os.getenv("REDIS_PASSWORD"),
         ssl_certfile="./redis_user.crt",
         ssl_keyfile="./redis_user_private.key",
         ssl_ca_certs="./redis_ca.pem",
      )

   def createItem(self, itemName:str, itemDescription:str, itemPrice:float, itemImage:str):
      # code to create item in Redis
      self.r.lpush("NamesList", itemName)
      self.r.lpush("DescrList", itemDescription)
      self.r.lpush("PriceList", itemPrice)
      self.r.lpush("ImgUrlList", itemImage)

      return True

   def searchItem(self, itemName):
      if self.r.lpos("NamesList", itemName, count=0) != None:
         return self.r.lpos("NamesList", itemName, count=0)
      elif self.r.lpos("DescrList", itemName, count=0) != None:
         return self.r.lpos("DescrList", itemName, count=0)
      else:
         return None
