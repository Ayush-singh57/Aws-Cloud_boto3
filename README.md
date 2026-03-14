# AWS Boto3 Automation Portfolio

This repository contains a comprehensive collection of Python automation scripts using the AWS Boto3 SDK.its automated resource management across major AWS services.


## Project Structure

This repository is organized into **6 major AWS service domains**, each focusing on automation tasks commonly used by Cloud Engineers.

### IAM - Identity and Access Management

Automates creation and management of AWS identities and permissions.

**Features**

* Automated creation of IAM users and roles
* Trust policy configuration
* Permission attachment
* Secure teardown scripts for cleanup

---

### EC2 - Compute Automation

Scripts for **virtual machine lifecycle management** and automated infrastructure provisioning.

**Features**

* Launch and terminate EC2 instances
* Automated web server setup using **UserData scripts**
* Instance monitoring automation
* Cost optimization scripts

---

### S3 - Object Storage Automation

Automation for **AWS object storage operations and secure file sharing**.

**Features**

* S3 bucket creation and deletion
* File upload and download automation
* Bucket policy configuration
* Secure file sharing using **Presigned URLs**

---

### DynamoDB - NoSQL Database Automation

Demonstrates serverless database operations using the **Boto3 Resource Interface**.

**Features**

* Create DynamoDB tables
* CRUD operations (Create, Read, Update, Delete)
* Query and scan automation
* Table deletion scripts

---

### Serverless - Lambda and API Gateway

Automated deployment of **serverless applications**.

**Features**

* Deploy AWS Lambda functions
* Configure execution roles
* Automate API Gateway endpoint creation
* Create fully functional REST APIs

---

### CloudWatch - Monitoring and Observability

Automation for **AWS monitoring, alerts, and notifications**.

**Features**

* Create custom CloudWatch metrics
* Configure SNS topic subscriptions
* Automated CPU utilization alarms
* Real-time infrastructure monitoring

---

## Tech Stack

| Technology | Usage                |
| ---------- | -------------------- |
| Python 3.x | Automation scripts   |
| AWS        | Cloud infrastructure |
| Boto3      | AWS SDK for Python   |
| IAM        | Access management    |
| EC2        | Compute services     |
| S3         | Object storage       |
| DynamoDB   | NoSQL database       |
| Lambda     | Serverless compute   |
| CloudWatch | Monitoring           |

