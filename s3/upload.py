import boto3

BUCKET_NAME = "boto3-learning-bucket-7b5deb67"
LOCAL_FILE = "sample.txt"
S3_OBJECT_NAME = "uploaded_file.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def upload_to_s3():
    """
    Goal: Move a local file into the AWS Cloud.
    """
    print(f" Preparing to upload {LOCAL_FILE} to {BUCKET_NAME}...")
    
    try:
        # Perform the upload
        s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_OBJECT_NAME)
        print(f" Success! File is now available in S3 as '{S3_OBJECT_NAME}'.")
        
    except FileNotFoundError:
        print(f" Error: The file '{LOCAL_FILE}' was not found on your computer.")
    except Exception as e:
        print(f" Upload failed: {e}")

if __name__ == "__main__":
    upload_to_s3()