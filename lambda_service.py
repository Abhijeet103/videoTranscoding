import subprocess
import uuid
from email.utils import unquote
from upload_service  import upload_file_to_output_s3

import  boto3


s3 = boto3.client('s3')


def run_ffmpeg(input_path, output_path, resolution):
    cmd = ["/opt/ffmpeg" , "-i" , input_path , "-vf" , f"scale=-2{resolution}"  ,
           "-c:v" , "libx264" , "-preset" , "fast" , "-crf" , "23" , "-c:a" , "aac" ,
           "-b:a" , "128k" , output_path
           ]

    subprocess.run(cmd , check=True)



def lambda_handler(event, context):
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = unquote(record["s3"]["object"]["key"])


    input_path = "tmp/input.mp4"
    output_480 = "tmp/output_480.mp4"
    output_720 = "tmp/output_720.mp4"

    s3.download_file(bucket, key, input_path)

    run_ffmpeg(input_path, output_480, "480")
    run_ffmpeg(input_path, output_720, "720")

    name = uuid.uuid4()
    url_480= upload_file_to_output_s3(output_480 , name + "_480.mp4" )
    url_720 =upload_file_to_output_s3(output_720 , name + "_720.mp4" )

    # Save it in db


