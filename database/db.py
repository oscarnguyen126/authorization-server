import boto3
from os import getenv
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.client('dynamodb',
                    region_name=getenv('DB_REGION_NAME'),
                    aws_access_key_id=getenv('DB_ACCESS_KEY_ID'),
                    aws_secret_access_key=getenv('DB_SECRET_ACCESS_KEY'))


table = {
    "TableName": "users",
    "KeySchema": [
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'created_at',
            'KeyType': 'RANGE'
        },
    ],
    "AttributeDefinitions": [
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'created_at',
            'AttributeType': 'S'
        }
    ],
}

def create_tables():
    tables, _ = dynamodb.list_tables().values()
    if table['TableName'] not in tables:
        dynamodb.create_table(
            TableName=table["TableName"],
            KeySchema=table["KeySchema"],
            AttributeDefinitions=table["AttributeDefinitions"],
            BillingMode='PAY_PER_REQUEST'
        )
