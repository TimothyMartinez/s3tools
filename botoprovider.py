import boto3

class Boto:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def return_client(self):
        return self.s3

