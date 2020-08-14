#!/c/Python38/python

import sys
import boto3
import botocore

s3 = boto3.client('s3')

def addFiles(bucket, file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except Exception as e:
        if "NoSuchBucket" in str(e):
            print("Bucket does not exist")
        return False
    return True

bucketname = sys.argv[1]
filetoadd = sys.argv[2]
if addFiles(bucketname, filetoadd):
    print(filetoadd + " has been uploaded")
else:
    print(filetoadd + " could not be uploaded")