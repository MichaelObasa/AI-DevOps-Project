# AI-DevOps-Project

This project is a hands-on exploration of building secure, scalable, cost-aware infrastructure for AI-native tools using modern DevOps practices.

Instead of treating AI apps like demos, this project treats them like production-grade software — complete with CI/CD, containerization, secrets management, and token-level cost tracking.

🔧 What This Project Covers
Component	Description
✅ FastAPI App	Lightweight API to process prompts, return GPT-style responses
✅ Prompt Versioning	Hashing and storing prompt templates for rollback and history
✅ Token Usage Logging	Basic tracking of prompt/response token cost for cost monitoring
✅ Dockerized App	Containerized workflow for clean deployment
✅ GitHub Actions CI/CD	On-push pipeline for testing and deployment
🔒 Secrets Management (Vault)	(To be added) Secure handling of API keys and sensitive credentials
☁️ AKS Deployment	(Optional) For cloud-based scaling using Azure Kubernetes Service

📁 Project Structure
bash
Copy
Edit

ai-devops-pipeline/
├── app/
│   └── main.py            # FastAPI app
├── prompts/               # Saved prompt versions (SHA hashed)
├── logs/                  # Token usage logs
├── scripts/               # Utility scripts (e.g., rollback, analytics)
├── .github/workflows/     # GitHub Actions CI/CD pipeline
├── Dockerfile             # Container config
├── requirements.txt       # Python dependencies
└── README.md              # This file
🚀 How to Run It Locally
bash

Copy

Edit

# 1. Clone the repo
git clone https://github.com/MichaelObasa/ai-devops-pipeline.git
cd ai-devops-pipeline

# 2. Build and run with Docker
docker build -t ai-devops-app .
docker run -p 8000:8000 ai-devops-app

# 3. Test the API
curl -X POST http://localhost:8000/prompt \
-H "Content-Type: application/json" \
-d '{"prompt": "What is DevOps?"}'
✅ Example Response
json
Copy
Edit
{
  "version_id": "9baf8c3d",
  "response": "Mock GPT response to: What is DevOps?",
  "tokens_used": 10
}
📦 GitHub Actions
This project uses a simple CI/CD workflow to:

Install dependencies

Run basic build/test checks

Future steps: auto-deploy to AKS or Docker container registry

🧠 Why This Matters
LLM-powered apps are going mainstream — but most lack proper infrastructure around them.

This project shows how to:

Treat AI apps like real software

Deploy cleanly with CI/CD

Track prompt cost at a granular level

Build repeatable, production-friendly systems

📚 What’s Next
 Integrate HashiCorp Vault for secrets management

 Deploy to Azure Kubernetes Service (AKS)

 Add cost aggregation dashboard (Grafana or CSV)

 Publish full write-up on Medium

 Share key takeaways on LinkedIn
