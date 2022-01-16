import os
import boto3

# instantiate S3 connection (using
client = boto3.client('s3')

# set your current working dir, filepath and target bucket name
cur_path = os.getcwd()
file = 'profiles_007.csv'
filename = os.path.join(cur_path, 'data', file)
bucket = 's3-osk-bucket-3000'

# open the file you're about to upload
data = open(filename, 'rb')

# load the file into S3
client.upload_file(filename, bucket, file)
