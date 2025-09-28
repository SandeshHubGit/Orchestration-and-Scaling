import boto3
import random
import time

cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')

def push_custom_metric():
    while True:
        response_time = random.uniform(0.1, 0.9)
        cloudwatch.put_metric_data(
            Namespace='MicroserviceApp',
            MetricData=[
                {
                    'MetricName': 'ResponseTime',
                    'Dimensions': [
                        {'Name': 'ServiceName', 'Value': 'BackendAPI'},
                    ],
                    'Value': response_time,
                    'Unit': 'Seconds'
                },
            ]
        )
        print(f"Pushed metric: ResponseTime={response_time:.3f}s")
        time.sleep(60)

# Uncomment to run loop
# push_custom_metric()