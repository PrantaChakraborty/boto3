import os
import boto3

# method to upload file along with directory on s3 bucket
def upload_directory_to_s3(directory_path, bucket_name):
    access_key = ''
    secret_access_key = ''
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            key = os.path.relpath(file_path, directory_path)
            s3.upload_file(file_path, bucket_name, key)
            print(f"Uploaded {file_path} to S3 bucket {bucket_name} with key {key}")

# Usage
directory_path = ''
bucket_name = ''

upload_directory_to_s3(directory_path, bucket_name)
