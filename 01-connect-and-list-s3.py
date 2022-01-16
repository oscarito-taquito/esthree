import boto3

# instantiate client
client = boto3.client('s3')

# retrieve all bucket Metadata
response = client.list_buckets()

# loop through bucket data and display info and name
for b in response['Buckets']:
    print(b)

# list your buckets and compare on console
for n in response['Buckets']:
    print(n['Name'])
