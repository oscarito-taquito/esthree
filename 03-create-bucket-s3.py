import boto3

# instantiate S3 connection
client = boto3.client('s3')

# set bucket name
bucket = 's3-storage-osk-4000'

# create new bucket
client.create_bucket(
    Bucket=bucket
)

# retrieve bucket Metadata
response = client.list_buckets()

# list out bucket names
for b in response['Buckets']:
    print(b['Name'])
