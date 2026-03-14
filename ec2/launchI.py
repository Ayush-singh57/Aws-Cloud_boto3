import boto3

# Configuration
REGION = 'ap-south-1'

# We use two services now: SSM (to find the AMI) and EC2 (to launch the server)
ssm_client = boto3.client('ssm', region_name=REGION)
ec2 = boto3.resource('ec2', region_name=REGION)

def get_latest_ami():
    """
    Pro-Tip: Instead of hardcoding an AMI ID that might expire or have typos,
    we use AWS Systems Manager (SSM) to fetch the absolute latest 
    Amazon Linux 2023 image ID dynamically!
    """
    response = ssm_client.get_parameter(
        Name='/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'
    )
    return response['Parameter']['Value']

def launch_new_server():
    """
    Goal: Programmatically launch a new virtual server safely.
    """
    print("🔍 Fetching the latest Amazon Linux AMI ID from AWS SSM...")
    
    try:
        # Get the ID dynamically!
        dynamic_ami_id = get_latest_ami()
        
        # Upgraded to t3.micro to match modern AWS Free Tier requirements
        print(f"🚀 Launching a new t3.micro server using AMI: {dynamic_ami_id}...")
        
        # We use 'resource' here because it's easier for creating objects
        instances = ec2.create_instances(
            ImageId=dynamic_ami_id,
            InstanceType='t3.micro', # <--- Changed from t2.micro to t3.micro
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'My-Boto3-Lab-Server'},
                    {'Key': 'Environment', 'Value': 'Dev'}
                ]
            }]
        )
        
        new_instance = instances[0]
        print(f"✅ Success! New instance created with ID: {new_instance.id}")
        print("Wait a few minutes for it to reach 'running' state.")
        
    except Exception as e:
        print(f"❌ Launch failed: {e}")

if __name__ == "__main__":
    launch_new_server()