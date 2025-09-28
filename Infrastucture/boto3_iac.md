# ☁️ Step 5: Infrastructure as Code (IaC) using Python + Boto3

This step uses Python and Boto3 to define and provision the AWS infrastructure required for deploying the MERN microservices application.

---

## ✅ 1. Pre-requisites

Ensure the following before running the scripts:
- Python 3 installed
- `boto3` installed via `pip3 install boto3`
- AWS credentials configured via `aws configure`
- IAM user has EC2 and VPC full permissions

---

## ✅ 2. Create VPC, Subnets, and Internet Gateway

📄 `create_vpc.py`
```python
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

# Create VPC
vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc_response['Vpc']['VpcId']
print(f"✅ VPC created: {vpc_id}")

# Create Internet Gateway
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
print(f"🌐 IGW attached: {igw_id}")

# Create Subnet
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc_id)
subnet_id = subnet['Subnet']['SubnetId']
print(f"📦 Subnet created: {subnet_id}")

# Create Route Table and associate with Subnet
rtb = ec2.create_route_table(VpcId=vpc_id)
rtb_id = rtb['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=rtb_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
ec2.associate_route_table(RouteTableId=rtb_id, SubnetId=subnet_id)
print(f"🛣️ Route table set: {rtb_id}")
```

---

## ✅ 3. Create Security Group

📄 `create_sg.py`
```python
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
```

---

## ✅ 4. Create Launch Template and Auto Scaling Group

📄 `create_asg.py`
```python
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
asg = boto3.client('autoscaling', region_name='ap-south-1')

lt = ec2.create_launch_template(
    LaunchTemplateName='mern-launch-template',
    LaunchTemplateData={
        'ImageId': 'ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI
        'InstanceType': 't2.micro',
        'SecurityGroupIds': ['YOUR_SG_ID'],
        'KeyName': 'YOUR_KEY_NAME',
        'UserData': 'IyEvYmluL2Jhc2gKZWNobyAiU3RhcnRpbmcgTUVSTiBBcHAi'  # base64 shell script
    }
)

lt_id = lt['LaunchTemplate']['LaunchTemplateId']

asg.create_auto_scaling_group(
    AutoScalingGroupName='mern-backend-asg',
    LaunchTemplate={'LaunchTemplateId': lt_id, 'Version': '$Latest'},
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier='YOUR_SUBNET_ID'
)

print("🚀 Auto Scaling Group Created.")
```

---

## ✅ 5. Run the Scripts

```bash
python3 create_vpc.py
python3 create_sg.py
python3 create_asg.py
```

---

👉 Next: [Step 6 - Deploy Backend to ASG](../06_backend_asg)