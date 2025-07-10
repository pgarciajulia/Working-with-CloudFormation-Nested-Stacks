import os
import json
import requests

def lambda_handler(event, context):
    #msg = {'text': event['Records'][0]['Sns']['Message']}
    
    ip = event.get("queryStringParameters", {}).get("ip")
    source = event.get("queryStringParameters", {}).get("source")

    headers = {'Content-Type': 'application/json'}
    return {
        'statusCode': 200,
        "body": f"IP: {ip}, Source: {source}"
    }