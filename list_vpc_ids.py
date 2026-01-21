import boto3

# dont assume the client is 'vpc' 
vpc_client = boto3.client('ec2')

response = vpc_client.describe_vpcs()

vpcs = response['Vpcs']

for vpc in vpcs:
    print(vpc['VpcId'])