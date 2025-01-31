import boto3
#Define AWS service, s3 is being used
client = boto3.client('s3')

try:
#Request syntax
    response = client.create_bucket(
        Bucket='quote-gen'
    )
    print(response)
except Exception as e:
    print(f"Error: {e}")