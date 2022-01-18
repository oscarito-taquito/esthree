import boto3

# instantiate S3 connection
client = boto3.client('s3')

# path, bucket and file vars
target_bucket = 's3-osk-empty-bucket'

# retrieve bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])

client.delete_bucket(
    Bucket=target_bucket
)

# refresh bucket list and print out
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])
