import boto3

# instantiate S3 connection
client = boto3.client('s3')

target_bucket = 's3-osk-bucket-3000'
sub_folder_01 = 'example/'
sub_folder_02 = 'test/'

client.put_object(Bucket=target_bucket, Key=sub_folder_01)
client.put_object(Bucket=target_bucket, Key=sub_folder_02)

# retrieve all object metadata
all_objects = client.list_objects(Bucket=target_bucket)

# iterate through Contents Dictionary, Key value holds contents including subfolders
for a in all_objects['Contents']:
    print(a['Key'], a['LastModified'])
