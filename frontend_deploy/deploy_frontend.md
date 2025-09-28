# 🎨 Step 8: Deploy Frontend on EC2 Using Boto3

This step uses Boto3 to launch an EC2 instance that runs the frontend Docker container.

---

## ✅ Python Script: `deploy_frontend.py`

- Uses Amazon Linux 2 AMI
- Installs Docker
- Pulls image from Amazon ECR
- Runs frontend container on port 3000

---

## 🔧 Requirements

- Docker image must be pushed to ECR
- Replace:
  - `<ACCOUNT_ID>` with your AWS account ID
  - `YOUR_SG_ID`, `YOUR_SUBNET_ID`, `YOUR_KEY_NAME`

---

## 🖥️ Access

After instance launches:
```bash
http://<EC2-PUBLIC-IP>:3000
```

Use browser or `curl` to validate deployment.