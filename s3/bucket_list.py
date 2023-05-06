import boto3

# method to get bucket list
def get_bucket_list():
    access_key = ''
    secret_access_key = ''
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                    aws_secret_access_key=secret_access_key)
    
    response = s3.list_buckets()
    buckets = response['Buckets']
    for bucket in buckets:
        print(bucket)
    return None

# Usage
bucket_list = get_bucket_list()
print(bucket_list)
