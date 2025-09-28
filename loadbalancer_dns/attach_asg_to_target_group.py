import boto3

asg = boto3.client('autoscaling', region_name='ap-south-1')

asg.attach_load_balancer_target_groups(
    AutoScalingGroupName='mern-backend-asg',
    TargetGroupARNs=['YOUR_TG_ARN']
)
print("ASG attached to Target Group.")