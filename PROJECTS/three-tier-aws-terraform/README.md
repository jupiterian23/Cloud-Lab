# ☁️ Three-Tier AWS Architecture with Terraform

> 🚀 **Production-style AWS infrastructure built and managed entirely with Terraform (Infrastructure as Code).**

This project demonstrates the design, deployment, security, and validation of a **highly structured three-tier AWS architecture** using multiple Availability Zones, private application servers, a managed MySQL database, and an Application Load Balancer.

---

## 🏗️ Architecture

```text
                         🌐 INTERNET
                              │
                              ▼
                   ┌─────────────────────┐
                   │  ⚖️ Application      │
                   │     Load Balancer   │
                   │        (ALB)        │
                   │    PUBLIC SUBNETS   │
                   └──────────┬──────────┘
                              │
                         HTTP : 80
                              │
                              ▼
              ┌──────────────────────────────┐
              │       💻 APPLICATION TIER    │
              │                              │
              │  EC2 Instance A              │
              │  Private Subnet A            │
              │                              │
              │  EC2 Instance B              │
              │  Private Subnet B            │
              └──────────────┬───────────────┘
                             │
                        MySQL : 3306
                             │
                             ▼
              ┌──────────────────────────────┐
              │        🗄️ DATABASE TIER      │
              │                              │
              │      Amazon RDS MySQL        │
              │      PRIVATE SUBNETS         │
              └──────────────────────────────┘
```

### 🔐 Network Flow

```text
🌐 Internet
     │
     ▼
⚖️ ALB
     │
     │ HTTP :80
     ▼
💻 Private EC2
     │
     │ MySQL :3306
     ▼
🗄️ Private RDS
```

---

## 🎯 Project Objectives

The goal of this project was to gain hands-on experience designing and deploying AWS infrastructure using **Infrastructure as Code**.

### Key objectives:

* ☁️ Design a multi-tier AWS architecture
* 🔧 Automate infrastructure using Terraform
* 🌐 Configure VPC networking
* 🔒 Implement tier-based security
* ⚖️ Deploy an Application Load Balancer
* 💻 Deploy EC2 application servers
* 🗄️ Deploy a private RDS MySQL database
* 🔑 Implement IAM roles
* 🛠️ Access private EC2 instances using Systems Manager
* 🧪 Validate application and database connectivity
* 📚 Practice real-world AWS troubleshooting

---

## 🛠️ Technologies & AWS Services

| Category                   | Technologies                                 |
| -------------------------- | -------------------------------------------- |
| ☁️ Cloud                   | AWS                                          |
| 🏗️ Infrastructure as Code | Terraform                                    |
| 🌐 Networking              | VPC, Subnets, Route Tables, IGW, NAT Gateway |
| ⚖️ Load Balancing          | Application Load Balancer                    |
| 💻 Compute                 | Amazon EC2                                   |
| 🗄️ Database               | Amazon RDS MySQL                             |
| 🔐 Identity                | AWS IAM                                      |
| 🛡️ Security               | Security Groups                              |
| 🔧 Management              | AWS Systems Manager                          |
| 🐧 OS                      | Amazon Linux                                 |
| 💻 CLI                     | AWS CLI                                      |

---

## 🌐 VPC & Network Design

The infrastructure is deployed inside a custom VPC:

```text
VPC
10.0.0.0/16
│
├── 🌐 Public Subnets
│   ├── Public Subnet A
│   └── Public Subnet B
│
├── 💻 Private Application Subnets
│   ├── App Subnet A
│   └── App Subnet B
│
└── 🗄️ Private Database Subnets
    ├── DB Subnet A
    └── DB Subnet B
```

The architecture spans **two Availability Zones** to provide better availability and avoid depending on a single AZ.

---

## 🔐 Security Architecture

Security Groups control communication between each tier.

```text
🌐 INTERNET
     │
     │ HTTP :80 / HTTPS :443
     ▼
🛡️ ALB SECURITY GROUP
     │
     │ HTTP :80
     ▼
🛡️ APPLICATION SECURITY GROUP
     │
     │ MySQL :3306
     ▼
🛡️ DATABASE SECURITY GROUP
```

### Security principles implemented

* 🔒 Database is **not publicly accessible**
* 🔒 Application servers are deployed in **private subnets**
* 🔒 Database accepts traffic only from the application Security Group
* 🔒 ALB handles public HTTP traffic
* 🔑 EC2 uses an IAM role instead of storing AWS credentials
* 🛠️ Systems Manager provides administrative access to private EC2 instances

---

## ⚖️ Application Load Balancer

The Application Load Balancer distributes incoming HTTP traffic between two EC2 application servers.

```text
                 ⚖️ ALB
                /     \
               /       \
              ▼         ▼
          💻 EC2-A   💻 EC2-B
```

Both EC2 instances are registered as targets in the ALB target group.

The ALB health check uses:

```text
/
```

---

## 🗄️ Database Tier

The database tier uses **Amazon RDS for MySQL**.

Configuration highlights:

* 🗄️ MySQL 8.0
* 💾 20 GB initial storage
* 🔒 Private database subnets
* 🚫 Public access disabled
* 🔐 Port `3306`
* 🛡️ Access restricted to the Application Security Group

---

## 🧪 Infrastructure Validation

The deployed infrastructure was tested after deployment.

### ✅ ALB Test

The Application Load Balancer successfully served the application.

Example response:

```text
Three-Tier AWS Application
Application Server B
Managed by Terraform
```

### ✅ EC2 → RDS Connectivity

Connectivity from the private application server to the private RDS instance was successfully verified over:

```text
TCP :3306
```

### ✅ Systems Manager

AWS Systems Manager Session Manager was successfully used to connect to the private EC2 instance without requiring a publicly exposed SSH connection.

---

## 📁 Project Structure

```text
three-tier-aws-terraform/
│
├── 📄 README.md
│
├── 📂 application/
│   └── index.html
│
├── 📂 terraform/
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── vpc.tf
│   ├── subnets.tf
│   ├── routes.tf
│   ├── security_groups.tf
│   ├── iam.tf
│   ├── alb.tf
│   ├── ec2.tf
│   ├── rds.tf
│   ├── terraform.tfvars.example
│   └── .terraform.lock.hcl
│
└── 📂 architecture/
```

---

## 🚀 Deployment

### 1️⃣ Prerequisites

Install and configure:

* AWS CLI
* Terraform
* AWS credentials
* Appropriate AWS IAM permissions

### 2️⃣ Initialize Terraform

```bash
cd terraform
terraform init
```

### 3️⃣ Configure Variables

Create your local variable file:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Set your database credentials:

```hcl
db_username = "appadmin"
db_password = "YOUR_SECURE_PASSWORD"
```

> 🔒 **Never commit `terraform.tfvars` to GitHub.**

### 4️⃣ Review the Infrastructure

```bash
terraform plan
```

### 5️⃣ Deploy

```bash
terraform apply
```

### 6️⃣ View Outputs

```bash
terraform output
```

### 7️⃣ Destroy When Finished

```bash
terraform destroy
```

> ⚠️ AWS resources such as **NAT Gateways, RDS, ALB, and EC2** may incur charges. Destroy the infrastructure when the lab is complete.

---

## 📚 What I Learned

This project helped me gain practical experience with:

* ☁️ AWS VPC architecture
* 🌐 Public vs private subnet design
* 🛣️ Route tables and routing
* 🔄 NAT Gateway
* ⚖️ Application Load Balancing
* 💻 EC2 deployment
* 🗄️ RDS networking
* 🔐 IAM roles and policies
* 🛡️ Security Group design
* 🛠️ AWS Systems Manager
* 🏗️ Terraform Infrastructure as Code
* 🧪 Infrastructure validation
* 🐛 AWS networking troubleshooting

---

## 🔮 Future Improvements

Planned improvements for this project:

* 🧩 Refactor Terraform into reusable modules
* 🔐 Add HTTPS using AWS Certificate Manager
* 🌍 Add Route 53 DNS
* 📈 Add CloudWatch monitoring and alarms
* 🔄 Add EC2 Auto Scaling
* 🚀 Add CI/CD using GitHub Actions
* 🗃️ Implement Terraform remote state
* 🔍 Add infrastructure security scanning
* 🤖 Improve automated application deployment

---

## 👨‍💻 Author

### **Shubham Gorule**

🎓 BCA Student
☁️ Aspiring Cloud Engineer

**Focus Areas**

`AWS` · `Linux` · `Networking` · `Terraform` · `Docker` · `Kubernetes` · `DevOps` · `Cloud Security` · `AI Agents`

---

⭐ **If you find this project useful, feel free to explore the Terraform configuration and architecture.**
