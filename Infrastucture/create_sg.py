import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

sg = ec2.create_security_group(
    GroupName='mern-sg',
    Description='Allow web and app traffic',
    VpcId='YOUR_VPC_ID'
)
sg_id = sg['GroupId']

# Add inbound rules
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp', 'FromPort': 3000, 'ToPort': 3000, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp', 'FromPort': 5000, 'ToPort': 5000, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)
print(f"🛡️ Security Group Created: {sg_id}")