# DuFy 🎵

<img width="1887" height="811" alt="DuFy Banner" src="https://github.com/user-attachments/assets/026a908a-0428-4588-aa3f-05adda5f1032" />

**Live Demo:** [https://dufy.onrender.com/](https://dufy.onrender.com/)  
**GitHub Repository:** [https://github.com/preeyankakc037/Dufyy](https://github.com/preeyankakc037/Dufyy)

---

## About DuFy

DuFy is an **AI-powered music recommendation system** designed to solve a real problem in the music discovery industry. Many users, editors, and content creators struggle to find music that matches a specific mood, style, or theme, and even when they do, it often takes too much time or effort.  

The core goal of DuFy is **to automate music personalization at scale**—analyzing lyrics, metadata, and available audio across platforms (Spotify, YouTube, and other APIs) to cover **all available songs on the internet**. By leveraging **PyTorch embeddings and NLP-based similarity models**, DuFy aims to deliver highly accurate, context-aware, and personalized music recommendations efficiently.  

Currently, the system is trained on a curated dataset with embeddings (`music_embeddings.pt`), and the vision is to expand to **automatically process all available songs** online, making personalized music discovery seamless, fast, and effective for users and creators alike.

---

## Core Features

- **Personalized Music Recommendations** 🎵  
  - Trained on a dataset of songs using **PyTorch embeddings**.  
  - Converts song lyrics and metadata into **vector embeddings** for semantic similarity.  
  - Finds songs with similar mood, theme, or style based on user descriptions.  

- **Trending Spotify Tracks**  
  - Fetches Global Top 50 tracks from verified public playlists.  

- **REST API Endpoints**  
  - Exposes endpoints like `/api/recommend/` and `/api/trending/` for frontend integration.  

- **Scalable Infrastructure**  
  - Django + DRF backend, Redis caching, FAISS vector search for fast queries.  

---

## Tech Stack

- **Backend:** Django, Django REST Framework, SQLite/PostgreSQL  
- **Frontend:** HTML, Tailwind CSS, Bootstrap  
- **AI & NLP:** PyTorch, Sentence Transformers, Transformers (Hugging Face), scikit-learn  
- **Tools & Infrastructure:** Render, Git & GitHub  

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/preeyankakc037/Dufyy.git
cd Dufyy
