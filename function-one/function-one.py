import os
import json
import requests
import boto3
import random
import string

from codeguru_profiler_agent import with_lambda_profiler
#version 3
@with_lambda_profiler()

def lambda_handler(event, context):
    length = event.get("length", 12)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    #ip = event.get("queryStringParameters", {}).get("ip")
    ip = "181.91.126.65"
    source = event.get("queryStringParameters", {}).get("source")
    ec2 = boto3.client('ec2')

    # Get values from event (you can hardcode or pass them in via event)
    ip_address = ip       # e.g., "203.0.113.12"
    bgp_asn = event.get("bgp_asn", 65000)       # Optional default ASN
    device_name = event.get("device_name", "DeviceName-" + random_string)  # Optional
    gateway_type = "ipsec.1"

    for i in range(65535):
        print(f"Number: {i}")

    for i in range(65535):
        if i % 2 != 0:
            pares= pares + 1 
        else:
            impares= impares + 1 

    print (f"Pares: {pares}")
    print (f"imPares: {impares}")


    # Create the Customer Gateway
    #response = ec2.create_customer_gateway(
    #    BgpAsn=bgp_asn,
    #    PublicIp=ip_address,
    #    Type=gateway_type,
    #    DeviceName=device_name
    #)


    headers = {'Content-Type': 'application/json'}
    return {
        'statusCode': 200,
        "body": json.dumps({
            'CustomerGatewayId': response['CustomerGateway']['CustomerGatewayId'],
            'State': response['CustomerGateway']['State']
        })
    }