# import pip
# import os
# pip.main(['install', 'redis'])

import redis


import json
from dotenv import load_dotenv
import os
load_dotenv()


def createArrays(item):
    # code to create item in Redis
    r = redis.Redis(
        host='redis-10943.c60.us-west-1-2.ec2.cloud.redislabs.com',
        port=10943,
        password=os.getenv("REDIS_PASSWORD"),
        ssl_certfile="./redis_user.crt",
        ssl_keyfile="./redis_user_private.key",
        ssl_ca_certs="./redis_ca.pem",
    )
    r.set('foo', 'bar')
    # True

    # print(r.get('foo'))
    # b'bar'
    # return True if successful, False otherwise
    return True

createArrays("item1")
