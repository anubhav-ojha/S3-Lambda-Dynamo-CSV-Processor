import boto3
import csv
import json

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
# Name of your dynamoDB Table
table = dynamodb.Table('employeeDyanmoDb')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket = bucket, Key=key)
    data = obj['Body'].read().decode('utf-8')

    csvreader = csv.DictReader(data.splitlines())

    with table.batch_writer() as batch:
        for row in csvreader:
            json_row = json.dumps(row)
            batch.put_item(Item=json.loads(json_row)) 

    return 'Successfully processed {}'.format(key)        