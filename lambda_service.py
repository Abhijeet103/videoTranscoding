import subprocess

import  boto3



def run_ffmpeg(input_path, output_path, resolution):
    cmd = ["/opt/ffmpeg" , "-i" , input_path , "-vf" , f"scale=-2{resolution}"  ,
           "-c:v" , "libx264" , "-preset" , "fast" , "-crf" , "23" , "-c:a" , "aac" ,
           "-b:a" , "128k" , output_path
           ]

    subprocess.run(cmd , check=True)

