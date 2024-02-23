# import streamlit as st
# import boto3


# s3 = boto3.client(
#     's3',
#     region_name='ap-south-1',
#     aws_access_key_id='AKIAWSDTHUPLTKUZWMHP',
#     aws_secret_access_key='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'
# )

# st.title('S3 File Uploader')

# file = st.file_uploader("Upload File")

# if file is not None:
#     st.write("File uploaded successfully")

#     bucket_name = 'testsharvari'
#     filename = file.name
#     file_bytes = file.read()
#     s3.put_object(Bucket=bucket_name, Key=filename, Body=file_bytes)
    
#     st.write(f"File uploaded to S3: {filename}")
import boto3

session = boto3.Session(
    aws_access_key_id='AKIAWSDTHUPLTKUZWMHP',
    aws_secret_access_key='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',
)
s3 = session.resource('s3')
# Filename - File to upload
# Bucket - Bucket to upload to (the top level directory under AWS S3)
# Key - S3 object name (can contain subdirectories). If not specified then file_name is used
s3.meta.client.upload_file(Filename='C:\Sharvari\VIT\experiment\Reviews Data.csv', Bucket='testsharvari', Key='s3_output_key')