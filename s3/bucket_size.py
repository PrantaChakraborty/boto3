# method to get total size of a bucket
import boto3

def get_bucket_size(bucket_name):
    access_key = ''
    secret_access_key = ''

    # connect to AWS using access key and secret access key
    s3 = boto3.resource('s3',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_access_key)

    bucket = s3.Bucket(bucket_name)
    t_size = 0
    for b in bucket.objects.all():
        t_size += b.size
    return t_size


bucket_name = 'we-corporates'
print(get_bucket_size(bucket_name))
