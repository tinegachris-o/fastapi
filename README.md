# 🚀 FastAPI Media Upload API

A backend API built with **FastAPI** that supports user authentication, media uploads (images/videos), and a feed system.  
Files are stored using **ImageKit**, and user authentication is handled via **JWT** using `fastapi-users`.

---

## ✨ Features

- 🔐 JWT Authentication (Login, Register, Verify, Reset Password)
- 📤 Upload images & videos
- 🧑‍💻 Associate uploads with authenticated users
- 📰 Feed endpoint with all posts
- 🗑️ Delete posts (only by owner)
- ☁️ Cloud file storage via ImageKit
- ⚡ Async FastAPI + SQLAlchemy

---

## 🧠 Tech Stack

- **FastAPI**
- **SQLAlchemy (Async)**
- **SQLite** (development)
- **fastapi-users** (auth)
- **ImageKit** (file storage)
- **Uvicorn**

---

## 📁 Project Structure
App/
│── app.py # Main FastAPI app
│── db.py # Database models & session
│── schemas.py # Pydantic schemas
│── users.py # Auth setup (JWT, fastapi-users)
│── images.py # ImageKit configuration