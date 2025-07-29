# 🧠 AI x DevOps Project – Scalable Infra for LLM-Powered Apps

This project shows how to build secure, scalable, cost-aware infrastructure for AI-native tools using modern DevOps practices.

Instead of treating AI apps like demos, this project treats them like real software — with versioning, token usage tracking, CI/CD, and containerized deployment.

---

## 🔧 Features

- ✅ **FastAPI app** for handling LLM-style prompts
- ✅ **Prompt versioning** with SHA hash
- ✅ **Token usage logging** to CSV
- ✅ **Dockerized workflow**
- ✅ **CI/CD with GitHub Actions**
- 🔒 **Vault for secrets management** (planned)
- ☁️ **AKS deployment** (planned)

---

## 📁 Project Structure

ai-devops-pipeline/
├── app/
│ └── main.py
├── prompts/
├── logs/
├── scripts/
├── .github/workflows/
│ └── deploy.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy
Edit


---

## 🚀 Quick Start (Local)

```bash
# Clone the repo
git clone https://github.com/MichaelObasa/ai-devops-pipeline.git
cd ai-devops-pipeline

# Build the container
docker build -t ai-devops-app .

# Run the container
docker run -p 8000:8000 ai-devops-app

# Test with curl
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is DevOps?"}'

{
  "version_id": "a1b2c3d4",
  "response": "Mock GPT response to: What is DevOps?",
  "tokens_used": 10
}


