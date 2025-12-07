📌 Cloud Internet Client Reminder System (Django REST API)

A simple Django-based reminder system that helps cloud-internet service providers track clients, their subscription expiry dates, and automatically remind them when their renewal date is getting close.

This is my ALX Backend Capstone Project (Part 3 work).

🚀 Project Overview

This system allows a cloud-internet business owner to:

Add clients

Record their subscription start and end dates

Get reminders when a client’s subscription is about to expire

View, update, and delete clients

Connect the API to any frontend (React, Flutter, Thunkable, etc.)

🛠 Tech Stack

Django 6

Django REST Framework

SQLite (default for development)

CORS Headers (for frontend communication)

📁 Project Structure
client_reminder_system/
│
├── cloud_internet_reminder/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│
├── db.sqlite3
├── manage.py
└── README.md

✔️ Features
👥 Client Management

Create client

List all clients

Edit a client

Delete a client

⏰ Reminder System

Save subscription expiry date

Notify when expiry is near (via API response)

Can connect to SMS/email in future versions

🔧 Installation Instructions
1️⃣ Clone the repository
git clone https://github.com/appahchristian01-crypto/client_reminder_system.git
cd client_reminder_system

2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt


Or manually:

pip install django djangorestframework django-cors-headers

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start the server
python manage.py runserver

🌐 API Endpoints
Clients
Method	Endpoint	Description
GET	/api/clients/	List all clients
POST	/api/clients/	Create a new client
GET	/api/clients/<id>/	Get a single client
PUT	/api/clients/<id>/	Update client
DELETE	/api/clients/<id>/	Delete client
Reminders
Method	Endpoint	Description
GET	/api/reminders/	List reminders
POST	/api/reminders/	Create reminder
🧪 Testing the API

You can test using:

Postman

Insomnia

Curl

Your frontend app

Example request:

POST /api/clients/
{
  "name": "John Doe",
  "phone": "0541112222",
  "subscription_end": "2025-12-30"
}

📌 What I completed in Part 3 (ALX requirement)

Setup Django project

Added REST API structure

Implemented core models (Client + Reminder)

Built CRUD endpoints

Configured CORS

Pushed project to GitHub

🚀 Next Steps (Part 4)

Add authentication (JWT or DRF auth)

Add reminder notifications (SMS or email)

Create a frontend UI

Deploy to Render/Heroku

