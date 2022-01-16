import os
import boto3

# instantiate S3 connection
client = boto3.client('s3')

# path, bucket and file vars
target_bucket = 's3-osk-bucket-3000'

# list the contents of the subfolder
# retrieve all object metadata
all_objects = client.list_objects(Bucket=target_bucket)

# iterate through Contents Dictionary, Key value holds contents including sub-folders
print(f"List of objects in {target_bucket}:")
for a in all_objects['Contents']:
    print(a['Key'])


# enclose delete object in function
def del_file(filename):
    client.delete_object(
        Bucket=target_bucket,
        Key=filename
    )


# cli message
print('\nList of files to be deleted:')

# remove all files in example subdir
for a in all_objects['Contents']:
    if 'example/' in a['Key'] and a['Key'] != 'example/':
        print(f"file to be deleted: {a['Key']}")
        del_file(a['Key'])

# cli message
i = input('Press any key to continue deletion')

# refresh objects list
all_objects = client.list_objects(Bucket=target_bucket)

# cli message
print('\nRemaining Objects: ')
# print bucket contents
for a in all_objects['Contents']:
    print(a['Key'])
