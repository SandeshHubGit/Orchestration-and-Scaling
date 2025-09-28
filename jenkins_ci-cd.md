# 🛠️ Step 4: Jenkins Setup for CI/CD with Docker + CodeCommit + ECR

This step guides you to configure Jenkins for building and pushing Docker images to ECR automatically when changes are pushed to AWS CodeCommit repositories.

---

## ✅ 1. Launch Jenkins on EC2

### 🔸 Launch EC2 Instance
- Type: t2.medium or higher
- AMI: Ubuntu 20.04 or Amazon Linux 2
- Open ports: 22 (SSH), 8080 (Jenkins), 80 (optional)

### 🔸 SSH into the Instance
```bash
ssh -i your-key.pem ec2-user@<public-ip>
```

---

## ✅ 2. Install Jenkins

```bash
# Ubuntu
sudo apt update
sudo apt install openjdk-11-jdk -y
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

---

## ✅ 3. Install Required Tools on Jenkins EC2

```bash
sudo apt install docker.io -y
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### Also install:
```bash
sudo apt install git -y
sudo apt install awscli -y
pip3 install boto3
```

---

## ✅ 4. Setup Jenkins

- Open `http://<EC2-Public-IP>:8080`
- Unlock Jenkins using `/var/lib/jenkins/secrets/initialAdminPassword`
- Install Suggested Plugins
- Create Admin User

---

## ✅ 5. Install Jenkins Plugins

- AWS CodeCommit
- Docker Pipeline
- Pipeline
- GitHub Integration (optional)

---

## ✅ 6. Create Jenkins Pipeline Job

1. Go to Jenkins Dashboard → New Item → Pipeline
2. Name: `Build-Microservices`
3. Select “Pipeline” → OK

---

## ✅ 7. Configure Pipeline Script

Example `Jenkinsfile`:

```groovy
pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = 'YOUR_AWS_ACCOUNT_ID'
    }

    stages {
        stage('Clone Frontend') {
            steps {
                git credentialsId: 'codecommit-creds', url: 'https://git-codecommit.ap-south-1.amazonaws.com/v1/repos/micro-frontend'
            }
        }

        stage('Build & Push Frontend') {
            steps {
                sh '''
                docker build -t micro-frontend .
                docker tag micro-frontend:latest $AWS_ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
                aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com
                docker push $AWS_ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
                '''
            }
        }

        // Repeat stages for backend
    }
}
```

---

## ✅ 8. Trigger on CodeCommit Push (Optional)

- Set up a webhook or use polling (every few minutes)

---

👉 Next: [Step 5 - Infrastructure as Code using Boto3](../05_iac_boto3)