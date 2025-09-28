# 🌐 Step 7: Load Balancer + Route 53 DNS

This step covers setting up an Elastic Load Balancer (ELB) to route traffic to your backend ASG, and optionally connecting a custom domain using Route 53.

---

## ✅ 1. Create Target Group (via Boto3 or Console)

If using Boto3:
```python
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
```

---

## ✅ 2. Create Load Balancer (ALB)

```python
lb = elbv2.create_load_balancer(
    Name='mern-backend-alb',
    Subnets=['subnet-xxx', 'subnet-yyy'],  # Must be 2 AZs
    SecurityGroups=['YOUR_SG_ID'],
    Scheme='internet-facing',
    Type='application',
    IpAddressType='ipv4'
)

lb_arn = lb['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer ARN: {lb_arn}")
```

---

## ✅ 3. Create Listener for Load Balancer

```python
elbv2.create_listener(
    LoadBalancerArn=lb_arn,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': 'YOUR_TG_ARN'
        }
    ]
)
```

---

## ✅ 4. Attach ASG to Target Group

```python
asg = boto3.client('autoscaling')
asg.attach_load_balancer_target_groups(
    AutoScalingGroupName='mern-backend-asg',
    TargetGroupARNs=['YOUR_TG_ARN']
)
```

---

## ✅ 5. Validate Public DNS

Once the ALB is up and instances are healthy:

```bash
curl http://<ALB-DNS-NAME>
```

You should see a response from the backend.

---

## ✅ 6. (Optional) Route 53 Setup

1. Go to Route 53 → Create Hosted Zone
2. Add domain name and get NS records
3. Create A record → alias to the Load Balancer

---

👉 Next: [Step 8 - Deploy Frontend on EC2](../08_frontend_deploy)