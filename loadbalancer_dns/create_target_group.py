import boto3

elbv2 = boto3.client('elbv2', region_name='ap-south-1')

tg = elbv2.create_target_group(
    Name='mern-backend-tg',
    Protocol='HTTP',
    Port=5000,
    VpcId='YOUR_VPC_ID',
    HealthCheckProtocol='HTTP',
    HealthCheckPath='/',
    TargetType='instance'
)
print(f"Target Group ARN: {tg['TargetGroups'][0]['TargetGroupArn']}")