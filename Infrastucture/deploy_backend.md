# 🚀 Step 6: Deploy Backend Service on EC2 via Auto Scaling Group (ASG)

This step deploys the backend container on EC2 instances provisioned by an Auto Scaling Group (ASG) using the previously defined Launch Template.

---

## ✅ 1. Modify the Launch Template (Optional)

If your backend container requires ENV variables or startup scripts, edit the `UserData` in `create_asg.py`:

```bash
#!/bin/bash
yum update -y
yum install docker -y
systemctl start docker
docker run -d -p 5000:5000 <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/micro-backend
```

Then base64 encode the script:
```bash
cat script.sh | base64
```

Paste it into `UserData` of the Launch Template in the `create_asg.py` script.

---

## ✅ 2. Trigger ASG Creation (if not already done)

```bash
python3 create_asg.py
```

This spins up EC2 instances automatically using Launch Template.

---

## ✅ 3. Validate Backend Is Running

- Go to EC2 dashboard
- Open one instance → Public IP → `http://<public-ip>:5000`
- Check if the backend API is live

---

## ✅ 4. Logs (Optional)

SSH into the instance and run:
```bash
docker ps
docker logs <container-id>
```

---

👉 Next: [Step 7 - Networking with Load Balancer + Route 53](../07_loadbalancer_dns)