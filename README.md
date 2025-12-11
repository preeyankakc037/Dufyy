# DuFy: AI-Powered Music Recommendation System

Check out here====> https://dufy.onrender.com/
## 🎧 Overview
**DuFy** is an AI-powered music recommendation platform that delivers **personalized song suggestions** using **Natural Language Processing (NLP)** and **Machine Learning**.  
Unlike traditional recommendation systems that rely only on listening history or popularity, DuFy analyzes **lyrics**, **metadata**, and **emotional context** to suggest songs that match the user’s intent, theme, or mood.

Built as a **full-stack web application**, DuFy integrates:
- **Django + Django REST Framework (DRF)** for backend APIs  
- **React.js + Tailwind CSS** for the frontend interface  
- **NLP models (Sentence Transformers, Transformers)** for semantic similarity and intelligent recommendations  

---

## ⚙️ Workflow

### 1. Data Collection
A curated dataset of songs, including **lyrics, artist names, genres, and metadata**, is stored in a database (SQLite/PostgreSQL).

### 2. Preprocessing
Using NLP models, each song’s **lyrics are embedded** into numerical vectors that capture semantic meaning — such as emotions, topics, and themes.

### 3. Similarity Analysis
**Cosine similarity** measures the closeness between songs in the embedding space, enabling DuFy to find tracks that are similar in **emotion or lyrical content**.

### 4. Recommendation Engine
When a user provides a description or selects a song:
- The system processes the input using NLP  
- Finds songs with similar lyrical/semantic features  
- Returns a ranked list of recommended songs  

### 5. API Layer
**Django REST Framework** exposes endpoints (e.g., `/api/recommend/`) to serve recommendations to the frontend.

### 6. Frontend Display
**React** fetches results from the API and presents them in an interactive, user-friendly interface styled with **Tailwind CSS**.

---

## 💡 Vision
DuFy aims to make **music discovery more meaningful**, helping users explore songs that truly align with their feelings, creativity, or project needs — not just what’s trending.

---

**Tech Stack:** Django | DRF | React.js | Tailwind CSS | NLP (Sentence Transformers, Scikit-learn, Transformers)  
**Language:** Python (3.11)  
**Database:** SQLite / PostgreSQL  

---
