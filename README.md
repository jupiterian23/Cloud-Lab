# ☁️ Cloud-Lab

A hands-on **Cloud Engineering, DevOps, Linux, Networking, Kubernetes, Terraform, and AWS learning laboratory**.

This repository contains my practical learning journey, experiments, labs, notes, automation exercises, and cloud projects. The goal is to build real technical skills through implementation rather than relying only on theoretical learning.

---

## 🎯 Mission

The long-term goal of this laboratory is to develop practical expertise across:

```text
Linux
  ↓
Networking
  ↓
Python & Automation
  ↓
AWS
  ↓
Docker
  ↓
Kubernetes
  ↓
Terraform
  ↓
DevOps
  ↓
DevSecOps
  ↓
Cloud Architecture
  ↓
AI Agents for Cloud Operations
```

The focus is on **building, breaking, troubleshooting, securing, documenting, and improving real systems**.

---

# 🏗️ Repository Structure

```text
Cloud-Lab/
│
├── AWS/
│   ├── IAM/
│   ├── EC2/
│   ├── S3/
│   ├── VPC/
│   ├── RDS/
│   └── CLI/
│
├── DEVOPS/
│   ├── CI-CD/
│   ├── Automation/
│   └── DevSecOps/
│
├── DOCKER/
│   ├── Images/
│   ├── Containers/
│   ├── Networking/
│   └── Projects/
│
├── KUBERNETES/
│   ├── Pods/
│   ├── Deployments/
│   ├── Services/
│   ├── ConfigMaps/
│   ├── Secrets/
│   └── Projects/
│
├── LINUX/
│   ├── Administration/
│   ├── Networking/
│   ├── Nginx/
│   ├── Security/
│   └── Troubleshooting/
│
├── NETWORKING/
│   ├── TCP-IP/
│   ├── DNS/
│   ├── Subnetting/
│   ├── Routing/
│   └── CCNA/
│
├── TERRAFORM/
│   ├── AWS/
│   ├── Modules/
│   └── Projects/
│
├── PYTHON/
│   ├── Fundamentals/
│   ├── Automation/
│   └── Cloud/
│
├── PROJECTS/
│   ├── End-to-End-AWS-Cloud-DevSecOps-Project/
│   ├── AWS-Cloud-Infrastructure-Terraform/
│   ├── End-to-End-Kubernetes-Three-Tier-DevSecOps-Project/
│   └── Other Cloud Projects/
│
└── README.md
```

---

# ☁️ AWS

The AWS section contains hands-on exercises covering fundamental cloud infrastructure.

## Services Practiced

* IAM
* EC2
* VPC
* Subnets
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* S3
* RDS
* AWS CLI

## AWS CLI

AWS infrastructure is managed and tested using the AWS CLI.

Example:

```bash
aws sts get-caller-identity --profile shubham-admin
```

Example:

```bash
aws ec2 describe-vpcs \
  --profile shubham-admin \
  --region ap-south-1
```

The laboratory uses AWS resources carefully with a focus on:

* Cost awareness
* Free-tier usage where applicable
* IAM security
* Resource cleanup
* Infrastructure verification

---

# 🐧 Linux

Linux is treated as a core foundation for Cloud and DevOps engineering.

Topics practiced include:

* Filesystem
* Users and groups
* Permissions
* Processes
* Services
* Package management
* Networking
* SSH
* Logs
* System troubleshooting
* Nginx
* Server hardening
* Shell commands

Example:

```bash
systemctl status nginx
```

```bash
ss -tulpn
```

```bash
journalctl -u nginx
```

---

# 🌐 Networking

Networking fundamentals are an important part of the Cloud-Lab.

Topics include:

* TCP/IP
* OSI model
* IPv4
* Subnetting
* CIDR
* DNS
* DHCP
* Routing
* Ports
* Protocols
* NAT
* Firewalls
* Security Groups
* VPC networking

Example architecture:

```text
Internet
   |
   v
Internet Gateway
   |
   v
Public Subnet
   |
   v
EC2
```

Private architecture:

```text
Internet
   |
   v
Internet Gateway
   |
   v
NAT Gateway
   |
   v
Private Subnet
   |
   v
Private Resources
```

---

# 🐳 Docker

Docker is used to understand containerized application deployment.

Topics practiced:

* Images
* Containers
* Dockerfiles
* Container ports
* Volumes
* Networks
* Environment variables
* Health checks
* Image optimization
* Container troubleshooting

Example:

```bash
docker build -t cloud-operations-api:1.1 .
```

Run:

```bash
docker run -d \
  --name cloud-operations-api \
  -p 8000:8000 \
  cloud-operations-api:1.1
```

Check:

```bash
docker ps
```

---

# ☸️ Kubernetes

Kubernetes is used to learn container orchestration and cloud-native application operations.

Topics include:

* Pods
* Deployments
* ReplicaSets
* Services
* NodePort
* Namespaces
* ConfigMaps
* Secrets
* Health probes
* Service discovery
* Scaling
* Kubernetes networking
* Troubleshooting

Example:

```bash
kubectl get nodes
```

```bash
kubectl get pods -A
```

```bash
kubectl get deployments
```

```bash
kubectl get services
```

---

# 🏗️ Terraform

Terraform is used to practice Infrastructure as Code.

Topics include:

* Providers
* Resources
* Variables
* Outputs
* State
* Dependencies
* AWS infrastructure
* Infrastructure validation
* Infrastructure planning
* Infrastructure deployment

Typical workflow:

```bash
terraform init
```

```bash
terraform validate
```

```bash
terraform plan
```

```bash
terraform apply
```

Terraform state and sensitive variable files are excluded through `.gitignore`.

---

# 🔄 DevOps

The DevOps section focuses on connecting development and infrastructure operations.

Areas include:

* Git
* GitHub
* CI/CD
* Docker
* Kubernetes
* Terraform
* Automation
* Infrastructure as Code
* Deployment workflows
* Troubleshooting

Typical workflow:

```text
Developer
    |
    v
Git
    |
    v
GitHub
    |
    v
CI/CD
    |
    v
Build
    |
    v
Test
    |
    v
Security Scan
    |
    v
Container
    |
    v
Kubernetes
    |
    v
Monitoring
```

---

# 🔐 DevSecOps

Security is integrated into the Cloud-Lab rather than treated as a separate activity.

Areas include:

* IAM
* Least privilege
* Security Groups
* Linux permissions
* Server hardening
* Container security
* Vulnerability scanning
* Secret management
* Secure configuration
* Infrastructure security

Tools practiced include:

* Trivy
* AWS IAM
* Linux security tools
* Git security practices

---

# 🐍 Python

Python is used for programming fundamentals and cloud automation.

Areas include:

* Python fundamentals
* Functions
* OOP
* File handling
* APIs
* Automation
* AWS automation
* Cloud tooling

The goal is to use Python as an **engineering automation tool**, especially for Cloud and DevOps tasks.

---

# 🚀 Projects

The `PROJECTS/` directory contains larger practical implementations.

## End-to-End AWS Cloud DevSecOps Project

A complete cloud-native portfolio project combining:

```text
FastAPI
   ↓
Docker
   ↓
Security Scanning
   ↓
Kubernetes
   ↓
Terraform
   ↓
CI/CD
   ↓
Monitoring
   ↓
AWS
```

Repository:

`End-to-End-AWS-Cloud-DevSecOps-Project`

The project demonstrates a complete application deployment and operations workflow.

---

## AWS Cloud Infrastructure with Terraform

A Terraform-based AWS infrastructure project demonstrating Infrastructure as Code.

Areas include:

* AWS Provider
* S3
* Terraform configuration
* Variables
* Outputs
* State management
* Infrastructure deployment

---

## Kubernetes Three-Tier DevSecOps Project

A practical Kubernetes and DevSecOps project exploring:

* Kubernetes
* Application deployment
* Containerization
* Security
* CI/CD
* Infrastructure
* Cloud-native architecture

---

# 🧪 Hands-On Philosophy

This laboratory follows a practical learning approach.

Instead of only studying:

```text
Theory → Memorization
```

the preferred workflow is:

```text
Concept
   ↓
Build
   ↓
Test
   ↓
Break
   ↓
Troubleshoot
   ↓
Fix
   ↓
Document
   ↓
Repeat
```

Failures are treated as part of the learning process.

---

# 🛠️ Cloud-Lab Environment

Current laboratory environment includes:

| Tool           | Purpose                       |
| -------------- | ----------------------------- |
| Windows        | Host operating system         |
| WSL Ubuntu     | Linux development environment |
| Git            | Version control               |
| GitHub CLI     | Repository management         |
| AWS CLI        | AWS management                |
| Docker Desktop | Container runtime             |
| Kubernetes     | Container orchestration       |
| Kind           | Local Kubernetes clusters     |
| kubectl        | Kubernetes management         |
| Helm           | Kubernetes package management |
| Terraform      | Infrastructure as Code        |
| Ansible        | Configuration automation      |
| Python         | Automation and programming    |
| Node.js        | Application/tooling ecosystem |

---

# 🔧 Development Workflow

Typical workflow:

```text
1. Learn a concept
       ↓
2. Build a small lab
       ↓
3. Test the system
       ↓
4. Troubleshoot failures
       ↓
5. Document the solution
       ↓
6. Commit to Git
       ↓
7. Push to GitHub
       ↓
8. Turn successful labs into projects
```

---

# 📚 Documentation

Documentation is maintained alongside the practical work.

Documentation can include:

* Architecture diagrams
* Command references
* Troubleshooting notes
* Deployment guides
* Incident notes
* Configuration explanations
* Security notes
* Lessons learned

The goal is not simply to record commands, but to understand **why the system behaves the way it does**.

---

# 💰 Cost Awareness

Cloud resources are used carefully.

Before creating AWS infrastructure:

```text
Check resource
     ↓
Check pricing
     ↓
Check free-tier eligibility
     ↓
Create
     ↓
Test
     ↓
Verify
     ↓
Stop/Delete when finished
```

Particularly expensive resources are avoided or stopped when not required for active learning.

Local tools such as Kind and Docker are used whenever they provide a suitable alternative for practicing Kubernetes and container workflows.

---

# 📈 Learning Roadmap

The laboratory is continuously evolving.

```text
Phase 1
Linux + Networking
       ↓
Phase 2
AWS Fundamentals
       ↓
Phase 3
Docker
       ↓
Phase 4
Kubernetes
       ↓
Phase 5
Terraform
       ↓
Phase 6
DevOps + CI/CD
       ↓
Phase 7
DevSecOps
       ↓
Phase 8
Monitoring + Observability
       ↓
Phase 9
AWS Cloud Architecture
       ↓
Phase 10
AI Agents for Cloud Operations
```

---

# 🤖 Future: AI + Cloud Operations

A long-term area of exploration is combining AI agents with Cloud and DevOps workflows.

Potential areas include:

* Cloud monitoring agents
* Incident investigation
* Log analysis
* Infrastructure assistance
* Deployment assistance
* AWS operational automation
* Troubleshooting agents
* Security analysis
* Infrastructure documentation

The objective is to understand how AI can assist engineers while keeping infrastructure operations controlled, auditable, and secure.

---

# 📊 Skills Practiced

### Cloud

* AWS
* IAM
* EC2
* VPC
* S3
* RDS
* AWS CLI

### Infrastructure

* Terraform
* Infrastructure as Code
* Networking
* Linux administration

### Containers

* Docker
* Kubernetes
* Kind
* Helm

### DevOps

* Git
* GitHub
* CI/CD
* Automation

### Security

* IAM
* Linux hardening
* Container scanning
* DevSecOps

### Programming

* Python
* Bash
* FastAPI

### Operations

* Monitoring
* Health checks
* Troubleshooting
* Incident analysis

---

# 🏆 Project Philosophy

The purpose of Cloud-Lab is to move from:

```text
"I know the command."
```

to:

```text
"I understand what the command does,
why I am using it,
how the system works,
and how to troubleshoot it when it fails."
```

That mindset is the foundation of the laboratory.

---

# 📌 Repository Status

This repository is actively developed.

New labs, experiments, documentation, and projects are added as practical skills are developed.

---

# 👨‍💻 Author

## Shubham Ramakant Gorule

**BCA Student | Aspiring Cloud Engineer**

Current areas of focus:

* AWS
* Linux
* Networking
* Docker
* Kubernetes
* Terraform
* DevOps
* DevSecOps
* AI Agents
* Cloud Architecture

GitHub:

`https://github.com/jupiterian23`

---

# ⭐ Related Project

For the dedicated end-to-end portfolio implementation, see:

**End-to-End AWS Cloud DevSecOps Project**

`https://github.com/jupiterian23/End-to-End-AWS-Cloud-DevSecOps-Project`

---

## 🚀 Keep Building

```text
Learn → Build → Break → Fix → Document → Automate → Repeat
```

**Cloud-Lab is a continuous practical engineering journey.**
