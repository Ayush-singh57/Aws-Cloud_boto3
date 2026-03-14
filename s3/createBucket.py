import boto3
import uuid

# Configuration
REGION = 'ap-south-1'
s3 = boto3.client('s3', region_name=REGION)

def create_learning_bucket():
    
    unique_id = str(uuid.uuid4())[:8]
    new_bucket_name = f"boto3-learning-bucket-{unique_id}"
    
    print(f" Attempting to create")
    
    try:
        s3.create_bucket(
            Bucket=new_bucket_name,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print(f"Success! Bucket created in {REGION}.")
        return new_bucket_name
        
    except Exception as e:
        print(f"Failed to create bucket: {e}")
        return None

if __name__ == "__main__":
    create_learning_bucket()