import os
import json
import requests

def lambda_handler(event, context):
    #msg = {'text': event['Records'][0]['Sns']['Message']}
    msg = "Post"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(os.environ['TEAMS_WEBHOOK_URL'], headers=headers, data=json.dumps(msg).encode('utf-8'))
    return {
        'statusCode': 200,
        'body': "Teams message sent!"
    }