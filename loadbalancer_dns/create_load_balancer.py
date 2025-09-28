import boto3

elbv2 = boto3.client('elbv2', region_name='ap-south-1')

lb = elbv2.create_load_balancer(
    Name='mern-backend-alb',
    Subnets=['subnet-xxx', 'subnet-yyy'],
    SecurityGroups=['YOUR_SG_ID'],
    Scheme='internet-facing',
    Type='application',
    IpAddressType='ipv4'
)

lb_arn = lb['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer ARN: {lb_arn}")