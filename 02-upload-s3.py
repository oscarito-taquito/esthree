import os
import boto3

s3 = boto3.resource('s3')

cur_path = os.getcwd()
filename = os.path.join(cur_path, 'profiles_007.csv')
for bucket in s3.buckets.all():
    print(bucket.name)

data = open(filename, 'rb')
s3.Bucket('s3-storage-osk-play').put_object(Key='profiles_007.csv', Body=data)

