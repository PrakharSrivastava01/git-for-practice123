import boto3
from datetime import datetime
def list_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()["Buckets"]
    old_buckets = []
    new_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        new_buckets.append(bucket_name)

    return {
        "new_buckets": new_buckets,
    }
