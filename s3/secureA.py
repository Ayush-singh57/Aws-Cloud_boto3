import boto3

# Configuration
BUCKET_NAME = "boto3-learning-bucket-7b5deb67"
S3_OBJECT_NAME = "uploaded_file.txt"

s3 = boto3.client('s3', region_name='ap-south-1')

def create_secure_link():
    """
    Goal: Generate a Presigned URL. 
   """
    print(f"🔗 Generating a 1-hour secure link for {S3_OBJECT_NAME}...")
    
    try:
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': S3_OBJECT_NAME},
            ExpiresIn=3600  
        )
        print(" Success! ")
        print(f"\n{url}\n")
        
    except Exception as e:
        print(f" Link generation failed: {e}")

if __name__ == "__main__":
    create_secure_link()