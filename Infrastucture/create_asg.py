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