# 🐳 Step 2: Dockerize MERN Microservices & Push to Amazon ECR

This step walks you through containerizing both the frontend and backend services of the MERN microservices app and pushing them to AWS Elastic Container Registry (ECR).

---

## ✅ 1. Clone and Fork the Project

```bash
git clone https://github.com/<your-username>/SampleMERNwithMicroservices.git
cd SampleMERNwithMicroservices
```

---

## ✅ 2. Create Dockerfiles for Backend and Frontend

📁 `backend/Dockerfile`
```Dockerfile
FROM node:18

WORKDIR /app
COPY . .
RUN npm install

EXPOSE 5000
CMD ["npm", "start"]
```

📁 `frontend/Dockerfile`
```Dockerfile
FROM node:18

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
```

---

## ✅ 3. Authenticate Docker with Amazon ECR

```bash
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com
```

---

## ✅ 4. Create Amazon ECR Repositories

```bash
aws ecr create-repository --repository-name micro-backend
aws ecr create-repository --repository-name micro-frontend
```

---

## ✅ 5. Build Docker Images

```bash
# Backend
docker build -t micro-backend ./backend

# Frontend
docker build -t micro-frontend ./frontend
```

---

## ✅ 6. Tag Docker Images for ECR

```bash
docker tag micro-backend:latest <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-backend
docker tag micro-frontend:latest <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
```

---

## ✅ 7. Push Images to ECR

```bash
docker push <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-backend
docker push <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
```

---

## ✅ 8. ECR Image URLs

Make note of these image URLs:
```
micro-backend:   <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-backend
micro-frontend:  <aws_account_id>.dkr.ecr.ap-south-1.amazonaws.com/micro-frontend
```

You will use these in later steps for deploying to EC2 and EKS.

---

👉 Next: [Step 3 - Push code to AWS CodeCommit](../03_codecommit_repo)