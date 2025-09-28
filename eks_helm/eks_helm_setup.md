# ☸️ Step 10: Kubernetes (EKS) Deployment using eksctl + Helm

This step sets up an Amazon EKS (Elastic Kubernetes Service) cluster and deploys your containerized microservices using Helm charts.

---

## ✅ 1. Create EKS Cluster using `eksctl`

Install `eksctl`:
```bash
curl --silent --location "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
```

Create EKS cluster:
```bash
eksctl create cluster   --name microservices-cluster   --region ap-south-1   --nodegroup-name linux-nodes   --node-type t2.medium   --nodes 2   --nodes-min 1   --nodes-max 3   --managed
```

---

## ✅ 2. Configure `kubectl`

```bash
aws eks --region ap-south-1 update-kubeconfig --name microservices-cluster
kubectl get nodes
```

---

## ✅ 3. Install Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

---

## ✅ 4. Create Helm Chart (Optional)

You can package your frontend/backend microservices:
```bash
helm create micro-backend
helm create micro-frontend
```

Edit the `values.yaml` and `deployment.yaml` to point to your Docker images.

---

## ✅ 5. Deploy with Helm

```bash
helm install backend ./micro-backend
helm install frontend ./micro-frontend
```

Validate:
```bash
kubectl get pods
kubectl get svc
```

---

## 🧼 Cleanup

```bash
eksctl delete cluster --name microservices-cluster --region ap-south-1
```

---

Next: [Step 11 - Monitoring & Logging](../11_monitoring_cloudwatch)