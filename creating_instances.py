from helpers import * 

def create_instances(ec2_client, ami_type="Ubuntu", ami_amount=1):
    formatted_ami_type = ami_type.lower().strip().replace(" ", "")
    for i in range(ami_amount):
        if formatted_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif formatted_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif formatted_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("Unsupported AMI")
    
ec2_client = get_ec2_client()
create_instances(ec2_client)
create_instances(ec2_client, "Linux 2")
create_instances(ec2_client, ami_type="Linux 2023")

create_instances(ec2_client, ami_amount=2)
create_instances(ec2_client, ami_type="Linux 2023", ami_amount=3)