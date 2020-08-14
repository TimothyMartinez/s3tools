#!/c/Python38/python

import sys
import boto3
from botoprovider import Boto
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

def bucketExists(bucket_name):
    bucket = s3.Bucket(bucket_name)
    try:
        s3.meta.client.head_bucket(Bucket=bucket.name)
    except ClientError as e:
        return False
    return True

bucketFromBash = sys.argv[1]
if bucketExists(bucketFromBash):
    sys.exit(0)
else:
    sys.exit(1)