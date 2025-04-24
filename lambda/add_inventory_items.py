
import json
import os
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    data = json.loads(event['body'])
    item_id = str(uuid.uuid4())
    item = {
        'id': item_id,
        'name': data['name'],
        'quantity': data['quantity'],
        'location': data['location']
    }
    table.put_item(Item=item)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Item added', 'item': item})
    }
