import boto3

TABLE_NAME = "boto3-portfolio-table"

def create_table():
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{'AttributeName': 'UserId', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'UserId', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST' 
        )
        print(f"Creating table '{TABLE_NAME}'...")
        table.wait_until_exists() # Pauses script until AWS finishes
        print("Success: Table is ready.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_table()