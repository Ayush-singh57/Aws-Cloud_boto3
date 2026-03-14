import boto3

BUCKET_NAME = "your-bucket-name-here"
S3_OBJECT_NAME = "uploaded_file.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def cleanup_s3():
  
    try:
        # 1. Delete the object
        print(f" Deleting object: {S3_OBJECT_NAME}...")
        s3.delete_object(Bucket=BUCKET_NAME, Key=S3_OBJECT_NAME)
        
        # 2. Delete the bucket
        print(f" Deleting bucket: {BUCKET_NAME}...")
        s3.delete_bucket(Bucket=BUCKET_NAME)
        
        print(" Cleanup complete")
        
    except Exception as e:
        print(f" Cleanup failed: {e}")

if __name__ == "__main__":
    cleanup_s3()