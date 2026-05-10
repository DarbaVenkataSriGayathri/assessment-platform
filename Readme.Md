# Online Assessment Platform using Django REST Framework

## Project Overview

This is a backend-based Online Assessment Platform developed using Django and Django REST Framework.

The project allows:

* Admins to create exams
* Admins to add MCQ questions
* Students to attend exams
* REST APIs to retrieve exams and questions
* Automatic score evaluation

This project demonstrates:

* Python
* Django
* REST APIs
* SQL/SQLite
* OOPs
* Backend Development

---

# Tech Stack

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| Python                | Backend Programming     |
| Django                | Web Framework           |
| Django REST Framework | REST APIs               |
| SQLite                | Database                |
| VS Code               | Development Environment |
| Git                   | Version Control         |
| GitHub                | Code Hosting            |

---

# Project Structure

```bash
assessment-platform/
│
├── config/
├── exams/
├── venv/
├── manage.py
└── db.sqlite3
```

---

# Features

* Exam Management
* Question Management
* REST APIs
* Database Integration
* Django Admin Panel
* Auto Evaluation Logic

---

# API Endpoints

## Get Exams

```bash
GET /api/exams/
```

---

## Get Questions

```bash
GET /api/questions/1/
```

---

## Submit Exam

```bash
POST /api/submit/1/
```

---

# Database Models

## Exam

* title
* description

## Question

* question_text
* option1
* option2
* option3
* option4
* correct_answer

## Result

* student
* exam
* score

---

# How to Run Locally

## Step 1 — Clone Repository

```bash
git clone <your-github-repo-url>
```

---

## Step 2 — Go to Project Folder

```bash
cd assessment-platform
```

---

## Step 3 — Create Virtual Environment

### Mac/Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 4 — Install Dependencies

```bash
pip install django djangorestframework
```

---

## Step 5 — Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Step 6 — Create Superuser

```bash
python manage.py createsuperuser
```

---

## Step 7 — Run Server

```bash
python manage.py runserver
```

---

# Admin Panel

Open:

```bash
http://127.0.0.1:8000/admin
```

---

# REST APIs

## Exams API

```bash
http://127.0.0.1:8000/api/exams/
```

---

## Questions API

```bash
http://127.0.0.1:8000/api/questions/1/
```

---

# GitHub Push Steps

## Step 1 — Initialize Git

```bash
git init
```

---

## Step 2 — Create .gitignore

Create file:

```bash
.gitignore
```

Add:

```bash
venv/
__pycache__/
db.sqlite3
*.pyc
```

---

## Step 3 — Add Files

```bash
git add .
```

---

## Step 4 — Commit Code

```bash
git commit -m "Initial commit"
```

---

## Step 5 — Create GitHub Repository

Go to GitHub and create a repository:

Example:

```bash
assessment-platform
```

---

## Step 6 — Connect Local Repo to GitHub

Replace YOUR_REPO_URL with your GitHub repository URL.

```bash
git remote add origin YOUR_REPO_URL
```

Example:

```bash
git remote add origin https://github.com/username/assessment-platform.git
```

---

## Step 7 — Push Code

```bash
git branch -M main
git push -u origin main
```

---

# Interview Explanation

## Project Explanation

“I developed an Online Assessment Platform backend using Django REST Framework. The application allows admins to manage exams and questions through Django Admin Panel. I implemented REST APIs for retrieving exams and questions, used SQLite database for storage, and designed relational models using Django ORM. The project helped me understand backend architecture, REST APIs, serializers, URL routing, and database integration.”

---

# Concepts Used

* Python
* Django
* REST APIs
* Django ORM
* Serializers
* URL Routing
* SQLite
* OOPs
* Backend Development
* API Testing

---

# Future Enhancements

* JWT Authentication
* React Frontend
* Timer-based Exams
* Leaderboard
* Docker Deployment
* AWS Deployment
* Webcam Proctoring

---

# Author

Suneel
