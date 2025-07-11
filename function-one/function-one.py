import os
import json
import requests
import boto3
import random
import string




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
    device_name = event.get("device_name", "MyCustomerGateway")  # Optional
    gateway_type = "ipsec.1"

    # Create the Customer Gateway
    response = ec2.create_customer_gateway(
        BgpAsn=bgp_asn,
        PublicIp=ip_address,
        Type=gateway_type,
        DeviceName=device_name
    )


    headers = {'Content-Type': 'application/json'}
    return {
        'statusCode': 200,
        "body": json.dumps({
            'CustomerGatewayId': response['CustomerGateway']['CustomerGatewayId'],
            'State': response['CustomerGateway']['State']
        })
    }