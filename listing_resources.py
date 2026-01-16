from helpers import *  # Import helper functions for AWS clients and API calls
from typing import List, Dict, Any


def print_bucket_names(s3_client: Any) -> None:
    """
    Retrieve and print the names of all S3 buckets in the AWS account.

    Demonstrates:
    - Using a list of strings
    - Iterating over a list
    - Printing values from a list

    :param s3_client: AWS S3 client (type intentionally set to Any for learning purposes)
    """
    # Get a list of bucket names (List[str])
    bucket_names: List[str] = list_buckets(s3_client)

    # Print each bucket name
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: Any) -> None:
    """
    Retrieve and print the instance IDs of all EC2 instances.

    Demonstrates:
    - Working with a list of dictionaries
    - Accessing dictionary values
    - Building a list from extracted data

    :param ec2_client: AWS EC2 client (type intentionally set to Any for learning purposes)
    """
    # List of EC2 instances, each represented as a dictionary
    instances: List[Dict[str, Any]] = describe_instances(ec2_client)

    # Store extracted instance IDs
    instance_ids: List[str] = []

    # Extract InstanceId from each instance dictionary
    for instance in instances:
        instance_ids.append(instance["InstanceId"])

    # Print each instance ID
    for instance_id in instance_ids:
        print(instance_id)


# Create AWS service clients
ec2_client: Any = get_ec2_client()
s3_client: Any = get_s3_client()

# Execute functions
print_bucket_names(s3_client)
print_instance_ids(ec2_client)
