# Adobe India Hackathon 2025 - Round 1B

## 🚀 Challenge: Persona-Driven Document Intelligence

This solution processes a collection of PDF documents and intelligently extracts and ranks the most relevant sections based on:
- A given **persona** (e.g., student, researcher)
- A defined **job-to-be-done** (e.g., prepare a literature review)

It outputs a structured JSON containing:
- Metadata (persona, documents, task, timestamp)
- Top-ranked relevant sections and summaries per document

---

## �� Folder Structure

app/
├── input/ # Contains persona.json and PDF files (ignored in Git)
├── output/ # Output location for output.json (ignored in Git)
├── summarize_persona_docs.py
Dockerfile
README.md

Build the Docker Image

docker build --platform linux/amd64 -t persona_summary:adobe25 .
 Run the Container
bash
Copy code
docker run --rm \
  --platform linux/amd64 \
  -v $(pwd)/app:/app \
  --network none \
  persona_summary:adobe25

Features
⛓️ Works offline (no network calls)

💾 Fully CPU-compatible (linux/amd64)

📚 Generalizes to any persona/task/domain

⚡ Executes within 60 seconds for 3–5 PDFs

🧠 Outputs structured, ranked sections + refined summaries

❗ Constraints Respected
✅ No GPU / No Internet access

✅ Works on amd64, 8 CPU, 16 GB RAM

✅ Model-free (lightweight, <1GB total)


