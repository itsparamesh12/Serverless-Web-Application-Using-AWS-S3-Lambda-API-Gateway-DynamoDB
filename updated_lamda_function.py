import json
import math
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('math')
def lambda_handler(event, context):
    mathResult = math.pow(int(event['base']), int(event['exponent']))
    response = table.put_item(
        Item={
            'id': str(mathResult)
            })
# return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }
