# 💾 Step 9: AWS Lambda for MongoDB Backup to S3

This Lambda function simulates a backup operation and uploads a file to S3 with a timestamped filename.

---

## ✅ Function Workflow

1. Generates a filename with timestamp
2. Simulates MongoDB backup (you should trigger this from an external Mongo host)
3. Uploads `.gz` file to specified S3 bucket

---

## 🔐 Required IAM Role Permissions

- `s3:PutObject`

---

## ⚠️ Note

For real MongoDB backups:
- Perform `mongodump` on the host EC2 instance
- Trigger Lambda to upload `.gz` via `boto3`

This example assumes the backup is externally created and just demonstrates **Lambda → S3** upload.

---

## 📂 Output Format

Uploaded to:
```
s3://your-backup-bucket-name/mongodb-backup-YYYY-MM-DD-HH-MM-SS.gz
```