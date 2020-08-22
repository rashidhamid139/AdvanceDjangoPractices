import boto3
import os

AWS_ACCESS_KEY_ID = 'AKIAZ4RUTQSV633OURNA'
AWS_SECRET_ACCESS_KEY = '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'

session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


client = session.client('s3')

# for file in os.listdir():
#     if file.endswith('.py'):
#         upload_file_bucket = 'youtube-dummy-bucket1'
#         upload_file_key = 'python/' + str(file)
#         client.upload_file(file, upload_file_bucket, upload_file_key)


for file in os.listdir('/home/rashid139/Desktop/API'):
    if file.endswith('.csv'):
        print(file)
        upload_file_bucket = 'youtube-dummy-bucket1'
        upload_file_key = 'CSV/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
