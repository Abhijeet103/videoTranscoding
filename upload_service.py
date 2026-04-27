import os
import uuid

import boto3

s3 = boto3.client('s3')

INPUT_BUCKET = os.environ['INPUT_BUCKET']
OUTPUT_BUCKET = os.environ['INPUT_BUCKET']
REGION = os.environ['REGION']

def upload_file_to_input_s3(filepath):
    key = f"uploads/{uuid.uuid4()}.mp4"
    s3.upload_file(filepath, INPUT_BUCKET, key)

    url = f"https://{INPUT_BUCKET}.s3.{REGION}amazonaws.com/{key}"

    return url


def upload_file_to_output_s3(filepath , file_name):
    key = f"uploads/{file_name}.mp4"
    s3.upload_file(filepath, OUTPUT_BUCKET, key)

    url = f"https://{OUTPUT_BUCKET}.s3.{REGION}amazonaws.com/{key}"
    return url

