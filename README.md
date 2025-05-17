# 📄 ASK-THE-DOC

A lightweight **Retrieval-Augmented Generation (RAG)** app that allows users to ask questions from their uploaded documents (`.pdf` or `.txt`). Powered by **Streamlit**, **ChromaDB**, **SentenceTransformers**, and optionally deployable with **Docker**.

## 📎 Demo File

A sample `.txt` file used in the demo video is included in the repository.
👉 [aboutme.txt](./aboutme.txt)
It contains the following text :
```
Hello my name is Devansh gaur
I am from Gurgaon
I am currently pursuing B.Tech Computer Science 
```
This file was uploaded to the deployed app to demonstrate how the RAG system extracts context and answers questions based on user-provided documents.

🚀 WORKING OF THE APPLICATION :

https://github.com/user-attachments/assets/b737b33a-c7f4-4d1b-b295-002160d333dc




---

## 🚀 Features

- Upload `.pdf` or `.txt` documents
- Extract content and generate semantic embeddings
- Ask natural language questions
- Get context-aware answers using a local vector store
- Streamlit-based clean web interface
- Docker-ready for seamless deployment

---

## 🛠️ Tech Stack

- `Python 3.10+`
- `Streamlit` for frontend
- `ChromaDB` as the vector store (replacing FAISS for Streamlit compatibility)
- `SentenceTransformers` (`all-MiniLM-L6-v2`) for generating embeddings
- `PyMuPDF` (`fitz`) for PDF parsing
- `Docker` for containerization
- `AWS EC2` for deployment

---

## 🖥️ Live Demo

The app is deployed and accessible on:

🔗 **[http://13.48.44.113:8501/](http://13.48.44.113:8501/)**

---

## 🖥️ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ASK-THE-DOC.git
cd ASK-THE-DOC

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```


## 🐳 Docker Setup
This app is fully containerized with Docker.
🔧 Build the Docker image:
```bash
docker build -t ask-the-doc .
```
Run the Docker container 
```bash
docker run -p 8501:8501 ask-the-doc
```
Then go to: http://localhost:8501

PROJECT STRUCTURE :
```
ASK-THE-DOC/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker setup
└── README.md              # This file

```











