# Orchestration-and-Scaling

# 🚀 MERN Microservices on AWS (CI/CD, EKS, Jenkins, Lambda, Boto3, CloudWatch)

This project demonstrates full deployment of a containerized MERN application with microservices architecture on AWS using Infrastructure-as-Code, CI/CD pipelines, monitoring, backups, and more.

---

## 📂 Project Structure (Folder-Based)

Each step is implemented as a separate folder:

```
├── 01_aws_cli_boto3/           # AWS CLI + Boto3 setup
├── 02_docker_ecr/              # Dockerfile, build & push to ECR
├── 03_codecommit/              # AWS CodeCommit repo setup
├── 04_jenkins_pipeline/        # Jenkins CI/CD pipeline on EC2
├── 05_iac_boto3/               # Boto3 scripts for infra (VPC, SG)
├── 06_backend_deploy_asg/      # Backend on EC2 via ASG
├── 07_loadbalancer_dns/        # Load Balancer + Route 53 DNS
├── 08_frontend_deploy/         # Frontend EC2 deployment
├── 09_lambda_db_backup/        # Lambda → MongoDB backup to S3
├── 10_k8s_eks_helm/            # EKS Cluster + Helm deployment
├── 11_monitoring_cloudwatch/   # Metrics, Logs, Alarms
├── 12_docs/                    # Architecture diagram, summary
```

---

## ✅ Complete Step-by-Step Breakdown

### 🔹 Step 1: AWS CLI & Boto3

- Install AWS CLI:
  ```bash
  aws configure
  ```
- Install Boto3 SDK:
  ```bash
  pip install boto3
  ```

---

### 🔹 Step 2: Docker + ECR

- Dockerize backend and frontend microservices using `Dockerfile`
- Push images to Amazon ECR
- Provided files:
  - `Dockerfile`
  - `build_push.sh`

---

### 🔹 Step 3: AWS CodeCommit

- Create repository using AWS Console or CLI
- Push full MERN project code
- Git credentials helper used for auth

---

### 🔹 Step 4: Jenkins on EC2

- EC2 Instance setup using user-data for Jenkins installation
- Plugins: Git, Docker, ECR, CodeCommit
- Jenkins jobs:
  - Auto-trigger build
  - Push Docker image to ECR

---

### 🔹 Step 5: Infrastructure as Code via Boto3

Python scripts to create:

- VPC
- Subnets
- Internet Gateway
- Security Groups
- IAM Roles

---

### 🔹 Step 6: Backend EC2 + Auto Scaling Group

- Launch template auto-pulls ECR image
- Auto Scaling Group ensures HA setup
- Health checks + load balancing

---

### 🔹 Step 7: Load Balancer + Route 53

- ALB configured via Boto3
- Target group assigned to ASG
- Route 53 domain configured to point to ALB DNS

---

### 🔹 Step 8: Frontend Deployment

- EC2 instance pulls frontend image
- NGINX reverse proxy for React app
- Public IP accessible via browser

---

### 🔹 Step 9: Lambda Function for MongoDB Backup

- Lambda (Python + Boto3) to:
  - Dump MongoDB backup
  - Upload to S3 with timestamp
- Triggered manually or by event

---

### 🔹 Step 10: Kubernetes (EKS) with Helm

- EKS Cluster created using `eksctl`
- Helm charts for:
  - micro-backend/
  - micro-frontend/
- Configurable `values.yaml`

---

### 🔹 Step 11: Monitoring & Logging (CloudWatch)

- Python script (`push_metrics.py`) pushes simulated backend response times
- CloudWatch alarms:
  - Thresholds for latency
  - Integrated with SNS
- Logs from EC2, Lambda, EKS forwarded

  
---

## 🔐 IAM Permissions Needed

| Role       | Permissions                             |
|------------|------------------------------------------|
| Jenkins EC2| ECR, EC2 read, CloudWatch                |
| Lambda     | S3 (full for backup), EC2 (snapshot)     |
| Boto3 User | IAM, EC2, ECR, VPC, CloudWatch           |

---

## 📘 Resources

- [AWS Boto3 SDK](https://boto3.amazonaws.com/)
- [Amazon EKS](https://eksctl.io/)
- [Helm Docs](https://helm.sh/docs/)
- [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/)
