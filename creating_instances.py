from helpers import *  # Import helper functions such as EC2 client creation and AMI launch helpers
from typing import Any


def create_instances(ec2_client: Any, ami_type: str = "Ubuntu", ami_amount: int = 1) -> None:
    """
    Create one or more EC2 instances based on the specified AMI type.

    This function normalizes the AMI type string and creates EC2 instances
    using helper functions for supported operating systems.

    Supported AMI types:
    - Ubuntu
    - Linux 2
    - Linux 2023

    Args:
        ec2_client (Any): A boto3 EC2 client used to create instances.
        ami_type (str, optional): The operating system type for the instance.
                                  Defaults to "Ubuntu".
        ami_amount (int, optional): Number of instances to create.
                                    Defaults to 1.

    Returns:
        None
    """

    # Normalize the AMI type string for consistent comparison
    formatted_ami_type = ami_type.lower().strip().replace(" ", "")

    # Loop to create the requested number of instances
    for i in range(ami_amount):

        # Create an Ubuntu EC2 instance
        if formatted_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")

        # Create an Amazon Linux 2023 EC2 instance
        elif formatted_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")

        # Create an Amazon Linux 2 EC2 instance
        elif formatted_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")

        # Handle unsupported AMI types
        else:
            print("Unsupported AMI")


# Create a reusable EC2 client using helper logic
ec2_client = get_ec2_client()

# Create a single Ubuntu instance (default behavior)
create_instances(ec2_client)

# Create a single Amazon Linux 2 instance
create_instances(ec2_client, "Linux 2")

# Create a single Amazon Linux 2023 instance using a keyword argument
create_instances(ec2_client, ami_type="Linux 2023")

# Create two Ubuntu instances
create_instances(ec2_client, ami_amount=2)

# Create three Amazon Linux 2023 instances
create_instances(ec2_client, ami_type="Linux 2023", ami_amount=3)
