import os
import uuid

import boto3

s3 = boto3.client('s3')

input_bucket = os.environ['INPUT_BUCKET']
output_bucket = os.environ['OUTPUT_BUCKET']
region = os.environ['REGION']

def upload_to_input_s3(file_path):
    key = f"uploads/{uuid.uuid4()}.mp4"
    s3.upload_file(file_path, input_bucket, key)
    url = f"https://{input_bucket}.s3.{region}.amazonaws.com/{key}"
    return url


def upload_to_output_s3(file_path):
    key = f"uploads/{uuid.uuid4()}.mp4"
    s3.upload_file(file_path, output_bucket ,  key)
    url = f"https://{output_bucket}.s3.{region}.amazonaws.com/{key}"
    return url


# s3 bucket
#     upload
#         nwjddjdj229.mp4


