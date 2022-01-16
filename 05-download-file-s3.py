import os
import boto3

# instantiate S3 connection
client = boto3.client('s3')

# path, bucket and file vars
target_bucket = 's3-osk-bucket-3000'
cur_path = os.getcwd()
file = 'profiles_007.csv'
filename = os.path.join(cur_path, 'downloads', file)

client.download_file(
    Bucket=target_bucket,
    Key=file,
    Filename=filename
)

# list the downloads directory contents
downloads_dir = os.path.join(cur_path, 'downloads')

for root, dirs, files in os.walk(downloads_dir):
    for filename in files:
        print(filename)
