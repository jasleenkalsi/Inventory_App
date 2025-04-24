
import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps({'items': response['Items']})
    }
