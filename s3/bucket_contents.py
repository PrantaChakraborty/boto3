# method to check contents in bucket
import boto3


def get_bucket_contents(bucket_name):
    access_key = ''
    secret_access_key = ''
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                    aws_secret_access_key=secret_access_key)
    
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        objects = response['Contents']
        for obj in objects:
            print(f"Object Key: {obj['Key']}")
    else:
        print("The bucket is empty.")

# Usage
bucket_name = ''
get_bucket_contents(bucket_name)
