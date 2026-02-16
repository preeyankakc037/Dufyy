# DuFy 🎵  
AI-Powered Semantic Music Recommendation for Creators

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![PyTorch](https://img.shields.io/badge/PyTorch-Embeddings-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![NLP](https://img.shields.io/badge/NLP-Semantic%20Search-purple)
![Status](https://img.shields.io/badge/Project-AI%20System-success)

<p align="center">
  <img src="https://github.com/user-attachments/assets/026a908a-0428-4588-aa3f-05adda5f1032" width="32%" />
  <img src="https://github.com/user-attachments/assets/012fb27b-6dee-414c-91ce-6b3b7a93ad00" width="32%" />
  <img src="https://github.com/user-attachments/assets/f17dc954-240b-4857-880e-2cf109d64c97" width="32%" />
</p>

**Live Demo:** https://dufy.onrender.com/

---

## 📌 Project Overview

DuFy is an AI-powered music recommendation system designed to help video editors and content creators discover songs using natural, descriptive queries instead of rigid genre tags.  

Rather than relying on traditional metadata filters, DuFy transforms lyrics and contextual descriptions into semantic vector embeddings, enabling mood-aware and theme-based music search.

---

## 🚀 What DuFy Does

- Converts song lyrics and metadata into **PyTorch-based embeddings**
- Uses **semantic similarity search (FAISS)** to match user queries
- Fetches trending Spotify tracks via API integration
- Exposes REST endpoints (`/api/recommend/`, `/api/trending/`)
- Delivers fast, scalable recommendations using Django + Redis caching

---

## 🧠 How It Works

1. Curated dataset with enriched song descriptions  
2. NLP embedding generation using Transformers  
3. Vector storage and similarity search via FAISS  
4. Ranked recommendations returned through API  

The system is currently trained on a curated embedding file (`music_embeddings.pt`), with a long-term vision of automating music ingestion and description generation at scale.

---

## 🏗️ Tech Stack

**Backend:** Django, Django REST Framework  
**AI/NLP:** PyTorch, Sentence Transformers, Hugging Face Transformers  
**Search:** FAISS  
**Database:** SQLite / PostgreSQL  
**Infrastructure:** Render  
**Frontend:** HTML, Tailwind CSS, Bootstrap  

---

## ⚙️ Installation

```bash
git clone https://github.com/preeyankakc037/Dufyy.git
cd Dufyy
```

Create virtual environment:

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set environment variables:

```bash
export DJANGO_SECRET_KEY="your_secret_key"
export SPOTIFY_CLIENT_ID="your_spotify_client_id"
export SPOTIFY_CLIENT_SECRET="your_spotify_client_secret"
```

Run server:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🌟 What Makes DuFy Different

- Designed specifically for **video editors and short-form creators**
- Uses semantic search instead of genre filtering
- Focuses on real-world descriptive queries
- Built with scalability in mind despite deployment constraints
- Research-driven development with iterative experimentation

DuFy is an early but meaningful step toward fully automated, intelligent music discovery.

---

**Author:** Priyanka Khatri, Smriti Basnet 

