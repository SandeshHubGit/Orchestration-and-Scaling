import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    bucket = 'your-backup-bucket-name'
    filename = f"mongodb-backup-{timestamp}.gz"

    # Simulating backup file creation (actual backup must be done externally)
    with open('/tmp/' + filename, 'wb') as f:
        f.write(b'Dummy backup content')

    # Upload to S3
    s3.upload_file('/tmp/' + filename, bucket, filename)

    print(f"✅ Backup uploaded: {filename}")