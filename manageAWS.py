# import pip
# import os
# pip.main(['install', 'boto3'])

import boto3

def uploadToAWS():
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

    # s3.meta.client.download_file('sunhacks2', 'voronoi.png', './hello.png')
    s3 = boto3.client('s3')
    strName = 'hello.py'
    s3.upload_file('./setupRedis.py', 'sunhacks2', strName)
    return "https://sunhacks2.s3.us-west-1.amazonaws.com/"+strName