from helpers import *  # Import helper functions for AWS client creation and API calls
from typing import Any, List, Dict


def print_bucket_names(s3_client: Any) -> None:
    """
    Retrieve and print the names of all S3 buckets in the AWS account.

    This function demonstrates working with a list returned from a helper
    function and iterating over that list to access each value.

    Args:
        s3_client (Any): A boto3 S3 client used to list S3 buckets.

    Returns:
        None
    """

    # Retrieve a list of S3 bucket names
    bucket_names: List[str] = list_buckets(s3_client)

    # Loop through the list and print each bucket name
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: Any) -> None:
    """
    Retrieve and print the instance IDs of all EC2 instances.

    This function demonstrates working with a list of dictionaries,
    extracting values from each dictionary, and storing them in a new list.

    Args:
        ec2_client (Any): A boto3 EC2 client used to describe EC2 instances.

    Returns:
        None
    """

    # Retrieve a list of EC2 instances (each instance is a dictionary)
    instances: List[Dict[str, Any]] = describe_instances(ec2_client)

    # Create an empty list to store instance IDs
    instance_ids: List[str] = []

    # Extract the InstanceId from each instance dictionary
    for instance in instances:
        instance_ids.append(instance["InstanceId"])

    # Loop through the instance ID list and print each ID
    for instance_id in instance_ids:
        print(instance_id)


# Create reusable AWS service clients using helper functions
ec2_client = get_ec2_client()
s3_client = get_s3_client()

# Print all S3 bucket names
print_bucket_names(s3_client)

# Print all EC2 instance IDs
print_instance_ids(ec2_client)
