import boto3
import os

BUCKET_NAME = "boto3-learning-bucket-7b5deb67"
S3_OBJECT_NAME = "uploaded_file.txt"
DOWNLOAD_NAME = "downloaded_from_aws.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def download_from_s3():
    """
    Goal: Pull a file from the AWS Cloud back down to your local computer.
    """
    print(f" Downloading {S3_OBJECT_NAME} from {BUCKET_NAME}...")
    
    try:
       
        s3.download_file(BUCKET_NAME, S3_OBJECT_NAME, DOWNLOAD_NAME)
        
        print(f" Success! File saved locally as: {DOWNLOAD_NAME}")
        print(f" Location: {os.path.abspath(DOWNLOAD_NAME)}")
        
    except Exception as e:
        print(f" Download failed: {e}")

if __name__ == "__main__":
    download_from_s3()