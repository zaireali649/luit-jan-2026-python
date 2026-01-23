import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print('Hello from Lambda!')

    # Create an S3 client using boto3.
    # This client allows us to interact with the Amazon S3 service.
    s3 = boto3.client('s3')

    # Call the S3 API to retrieve a list of all buckets owned by the AWS account.
    #
    # The response returned by list_buckets() has the following structure:
    #
    # {
    #     'Buckets': [
    #         {
    #             'Name': 'string',                # Name of the S3 bucket
    #             'CreationDate': datetime(...),   # When the bucket was created
    #             'BucketRegion': 'string',        # Region where the bucket exists
    #             'BucketArn': 'string'            # ARN of the bucket
    #         },
    #     ],
    #     'Owner': {
    #         'DisplayName': 'string',              # Account display name
    #         'ID': 'string'                        # Canonical user ID
    #     },
    #     'ContinuationToken': 'string',            # Token for pagination (if applicable)
    #     'Prefix': 'string'                        # Prefix used to filter buckets
    # }
    response = s3.list_buckets()

    # Extract the list of buckets from the response.
    # This is a list of dictionaries, where each dictionary
    # represents a single S3 bucket and its metadata.
    buckets = response["Buckets"]

    bucket_names = []

    # Iterate over each bucket in the list
    for bucket in buckets:
        # Print the bucket name.
        # Accessing the "Name" key from each bucket dictionary.
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])

    
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names)
    }