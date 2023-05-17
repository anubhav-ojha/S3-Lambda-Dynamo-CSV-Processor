import boto3
import csv
import uuid

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('csv-S3to-Dynamo')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file_name = event['Records'][0]['s3']['object']['key']
    csv_object = s3_client.get_object(Bucket=bucket, Key=csv_file_name)
    file_reader = csv_object['Body'].read().decode("utf-8")
    users = file_reader.split('\n')
    users = list(filter(None, users))

    #have to write in dynamodb table 

    for user in users:
        user_data = user.split(',')
        item_id = str(uuid.uuid4())
        table.put_item(Item = {
            
            "id" : item_id,
            "name" : user_data[1],
            "salary" : user_data[2]

        })
    return 'success'