import boto3  # Import the AWS SDK for Python to interact with AWS services

# dont assume the client is 'vpc'
# The EC2 client is used because VPC-related APIs (like describe_vpcs)
# are part of the EC2 service in AWS.
vpc_client = boto3.client('ec2')

# Call the EC2 API to retrieve information about all VPCs
# in the current AWS account and region.
response = vpc_client.describe_vpcs()

# Extract the list of VPCs from the API response.
# The 'Vpcs' key contains a list of dictionaries, where each
# dictionary represents a single VPC and its configuration.
vpcs = response['Vpcs']

# Loop through each VPC in the list
for vpc in vpcs:
    # Print the VPC ID.
    # 'VpcId' is the unique identifier for a VPC (e.g., vpc-0a1b2c3d4e).
    print(vpc['VpcId'])
