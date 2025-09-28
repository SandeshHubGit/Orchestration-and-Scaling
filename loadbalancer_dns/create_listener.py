import boto3

elbv2 = boto3.client('elbv2', region_name='ap-south-1')

elbv2.create_listener(
    LoadBalancerArn='YOUR_LB_ARN',
    Protocol='HTTP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': 'YOUR_TG_ARN'
        }
    ]
)
print("Listener created and forwarding to Target Group.")