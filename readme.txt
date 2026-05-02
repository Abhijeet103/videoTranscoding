1) upload a video(API)
2 ) save to s3
3) processing via AWS lambda
4) upload all transcoded videos to s3
5) save the Url in RDS
6) send an upload  confirmation email via ses


on upload to input bucket start the ffmpeg function to transcode the video
upload to output bucket save url in Model


cmd to run ensible

ansible-playbook -i inventory.ini playbook.yml \
  --private-key=ansible.pem \
  -u ec2-user

