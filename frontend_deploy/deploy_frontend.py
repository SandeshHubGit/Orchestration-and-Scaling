import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')

# User data script to run Docker container on startup
user_data_script = '''#!/bin/bash
yum update -y
yum install docker -y
systemctl start docker
$(aws ecr get-login --no-include-email --region ap-south-1)
docker run -d -p 3000:3000 <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
'''

instance = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='YOUR_KEY_NAME',
    SecurityGroupIds=['YOUR_SG_ID'],
    SubnetId='YOUR_SUBNET_ID',
    UserData=user_data_script
)

print("🚀 Frontend EC2 instance launched:", instance[0].id)