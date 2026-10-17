import boto3
import json

#connect to sqs 
sqs = boto3.client('sqs', region_name='eu-central-1')
keys = set()

def sqsfunc():
    
    messages = sqs.receive_message(
    QueueUrl='https://sqs.eu-central-1.amazonaws.com/443602378074/testqueueaj',
    MaxNumberOfMessages=10)
    for i in messages['Messages']:
        x = json.loads(i['Body'])
        y = json.loads(x['Message'])
        z = y['requestPayload']['Records']
        keyname = z[0]['s3']['object']['key']
        keys.add(keyname)
        
sqsfunc()
keys