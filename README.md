## 🚀 DevOpsFlow Pipeline Project

A complete end-to-end DevOps CI/CD pipeline implementation using modern tools like **Docker**, **GitHub Actions**, **Terraform**, **Trivy**, and **Kubernetes (via Helm)**. This project demonstrates how to build, test, scan, and deploy a simple Python Flask app in a fully automated workflow.

---

## 🛠️ Tech Stack

- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **IaC**: Terraform (local backend for personal project)
- **Security Scanning**: Trivy
- **Kubernetes Deployment**: Minikube + Helm
- **Monitoring**: Prometheus & Grafana (planned)
- **Language**: Python (Flask)

> 💡 _Note: This project uses a **local Terraform backend** and Minikube as the Kubernetes provider for simplicity and local testing. In production, it is recommended to use a **remote backend** such as **AWS S3** (for storing state) with **DynamoDB** (for state locking)._

---

## 🧱 Project Structure

```bash
DevOpsFlow-Pipeline/
├── app.py                     # Python Flask app
├── Dockerfile                 # Docker image build definition
├── .github/
│   └── workflows/
│       └── devops-pipeline.yml          # GitHub Actions pipeline
├── terraform-configs/
│   ├── backend.tf             # Local backend config (can be switched to S3)
│   ├── main.tf                # Infra definition
│   ├── provider.tf            # Minikube as K8s provider
│   ├── variables.tf           # Input variables
│   └── terraform.tfvars       # Variable values
├── tests/
│   └── test_app.py            # Unit tests
├── .gitignore
└── README.md
```

## 🚀 Project Workflow

**Provisioning Infrastructure:**  
Minikube was provisioned locally using Terraform for testing and development purposes. Although this project uses a local backend, it is recommended to configure a remote backend like **Amazon S3** with **DynamoDB** for production-grade state management and locking.

**Application Containerization:**  
A Python Flask application was containerized using Docker. The image is built and tagged through a CI/CD pipeline.

**Automated Testing & Security Scanning:**

- Unit tests were written using `pytest` and executed in the CI pipeline.
- Integrated **Trivy** to scan the Docker image for vulnerabilities before pushing.

**Helm Chart Deployment:**  
Developed a reusable and customizable **Helm chart** to manage Kubernetes deployments and services.

**CI/CD with GitHub Actions:**  
Implemented a GitHub Actions pipeline to:

- Run tests
- Build and tag Docker images
- Perform Trivy scanning
- Push the image to Docker Hub

**GitOps with ArgoCD:**  
Configured **ArgoCD** to continuously monitor the GitHub repository. Any changes in the Helm chart or Kubernetes manifests are automatically synchronized with the cluster.

---

## ⚙️ Getting Started

**Prerequisites**

- Docker
- Terraform
- Minikube
- Python 3.x
- GitHub CLI

**Clone & Run Locally**

```bash
git clone https://github.com/dupsy-hub/DevOpsFlow-Pipeline.git
cd DevOpsFlow-Pipeline
docker build -t flask-time-app .
docker run -p 8080:8080 flask-time-app
```

Visit: http://localhost:8080

---

## 🧪 Testing

```bash
pytest tests/test_app.py
```

> Make sure `pytest` is installed.

---

## 🔐 Trivy Scan

Trivy automatically scans the Docker image for vulnerabilities as part of the GitHub Actions workflow.

---

## 🧹 Clean Up

To destroy infrastructure provisioned with Terraform:

```bash
terraform destroy
```

Or run without confirmation prompts:

```bash
terraform destroy --auto-approve
```

If using a remote backend:

- Empty and delete your S3 bucket
- Delete the DynamoDB table

---

## 👤 Author

**Modupe Ilesanmi**  
AWS Certified (DevOps Engineer Professional, Solutions Architect Associate, Developer Associate) | Terraform Associate | KCNA  
GitHub: [@dupsy-hub](https://github.com/dupsy-hub)
