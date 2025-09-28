# 📊 Step 11: Monitoring & Logging with CloudWatch

This step enables custom monitoring and logging for your microservices using Amazon CloudWatch.

---

## ✅ 1. Push Custom Metrics

Use the provided Python script to push sample metrics.

```bash
python push_metrics.py
```

---

## ✅ 2. Create CloudWatch Alarms

Create an alarm using the AWS Console or CLI:
```bash
aws cloudwatch put-metric-alarm \
  --alarm-name HighResponseTime \
  --metric-name ResponseTime \
  --namespace "MicroserviceApp" \
  --statistic Average \
  --period 60 \
  --threshold 0.7 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 1 \
  --alarm-actions arn:aws:sns:ap-south-1:<ACCOUNT_ID>:NotifyMe \
  --dimensions Name=ServiceName,Value=BackendAPI
```

---

## 📘 Logging with CloudWatch Logs

Enable logs in ECS, Lambda, EC2, or Kubernetes using:

- CloudWatch agent on EC2
- `awslogs` driver for ECS
- Lambda → Logs tab

---

## 🔧 IAM Permissions

Required permissions:
- `cloudwatch:PutMetricData`
- `cloudwatch:GetMetricData`
- `logs:CreateLogStream`
- `logs:PutLogEvents`

---

## ✅ Verify

Check:
- Metrics → `MicroserviceApp/ResponseTime`
- Alarms → `HighResponseTime`
- Logs → for respective services