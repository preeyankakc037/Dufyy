# DuFy 🎵

<img width="1887" height="811" alt="image" src="https://github.com/user-attachments/assets/026a908a-0428-4588-aa3f-05adda5f1032" />


**Live Demo:** [https://your-deployed-app.vercel.app](https://your-deployed-app.vercel.app)  

DuFy is a **Django + DRF backend project** that provides music recommendations and trending Spotify tracks using a public playlist. Optimized for **FAISS search**, caching with Redis, and deployed for **Vercel**.

---

## Features

- Fetch **Global Top 50** trending Spotify tracks  
- Recommendation engine for personalized music  
- REST API endpoints with **Django Rest Framework**  
- Secure, production-ready settings for deployment  
- Redis caching for improved performance  
- Easy integration with frontend apps

---

## Tech Stack

- **Backend:** Python 3.x, Django 5.x, Django REST Framework  
- **API:** Spotify Client Credentials API  
- **Caching:** Redis  
- **Vector Search:** FAISS  
- **Deployment:** Vercel  

---

## Installation

1. Clone the repository:

bash
git clone https://github.com/YOUR_USERNAME/Dufyy.git
cd Dufyy

2. Create a virtual environment:
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate


3. Install dependencies:
   pip install -r requirements.txt

4. Set environment variables:
   export DJANGO_SECRET_KEY="your_secret_key"
  export SPOTIFY_CLIENT_ID="your_spotify_client_id"
  export SPOTIFY_CLIENT_SECRET="your_spotify_client_secret"

5. Apply migrations and run server:
python manage.py migrate
python manage.py runserver



