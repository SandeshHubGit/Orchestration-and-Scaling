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