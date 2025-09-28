# 📂 Step 3: Version Control with AWS CodeCommit

This step walks you through migrating your MERN microservices app source code to **AWS CodeCommit**, a managed Git-based version control service.

---

## ✅ 1. Pre-Requisites

- You must have AWS CLI configured with appropriate IAM permissions (`AWSCodeCommitFullAccess`)
- Git must be installed on your system

---

## ✅ 2. Create CodeCommit Repository

Create two repositories:
- One for **frontend**
- One for **backend**

```bash
aws codecommit create-repository --repository-name micro-frontend
aws codecommit create-repository --repository-name micro-backend
```

---

## ✅ 3. Clone the Empty CodeCommit Repos Locally

```bash
# Replace <region> with ap-south-1 and <account_id> with your AWS account ID

# Clone Frontend Repo
git clone https://git-codecommit.ap-south-1.amazonaws.com/v1/repos/micro-frontend
cd micro-frontend

# Copy contents from your actual frontend folder
cp -r ../SampleMERNwithMicroservices/frontend/* .

git add .
git commit -m "Initial commit - Frontend"
git push origin main
cd ..
```

```bash
# Clone Backend Repo
git clone https://git-codecommit.ap-south-1.amazonaws.com/v1/repos/micro-backend
cd micro-backend

# Copy contents from your backend folder
cp -r ../SampleMERNwithMicroservices/backend/* .

git add .
git commit -m "Initial commit - Backend"
git push origin main
```

---

## ✅ 4. Confirm Upload in AWS Console

- Go to **CodeCommit** → Click on both repos → Verify that files are pushed
- These repos will now be the **source of truth** for Jenkins CI in the next step

---

## 🧠 Pro Tip:
You can use one monorepo instead of two, depending on your team's structure.

---

👉 Next: [Step 4 - Jenkins Setup for CI/CD](../04_jenkins_ci)