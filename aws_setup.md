# 🌐 Step 1: AWS CLI + Boto3 Setup Instructions

This step ensures your local machine is ready to interact with AWS services using both the AWS CLI and Python's Boto3 SDK.

---

## ✅ 1. Install AWS CLI

**MacOS/Linux**:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Windows**:
- Download and install from: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

**Verify Installation**:
```bash
aws --version
```

---

## ✅ 2. Configure AWS CLI

```bash
aws configure
```

Enter the following:
- AWS Access Key ID: `<Your_Access_Key_ID>`
- AWS Secret Access Key: `<Your_Secret_Access_Key>`
- Default region: `ap-south-1`
- Output format: `json`

🧪 Test:
```bash
aws s3 ls
```

---

## ✅ 3. Install Python & Boto3

**Check Python version**:
```bash
python3 --version
```

**Install pip if not installed**:
```bash
sudo apt install python3-pip  # Debian/Ubuntu
```

**Install Boto3**:
```bash
pip3 install boto3
```

**Verify installation**:
```bash
python3 -c "import boto3; print(boto3.__version__)"
```

---

## ✅ 4. Store AWS Credentials Securely

For local development, credentials are stored in:
```
~/.aws/credentials
~/.aws/config
```

> In production (e.g. EC2, Lambda, Jenkins), prefer IAM roles instead of hardcoding credentials.

---

## ✅ 5. Setup Complete

You’re now ready to use:
- AWS CLI to manage infrastructure
- Python with Boto3 to automate AWS tasks

Proceed to [Step 2: Dockerize MERN App & Push to ECR](../02_containerization_ecr)