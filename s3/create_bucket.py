import boto3


# method to create bucket
def create_s3_bucket(bucket_name, region):
    access_key = ''
    secret_access_key = ''
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)
    
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(f"S3 bucket '{bucket_name}' created in region '{region}'.")

# Usage
bucket_name = ''
region = ''

create_s3_bucket(bucket_name, region)