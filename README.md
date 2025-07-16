# 🔗 URL Shortener API – Django + MySQL

This is a take-home assignment for Innovaxel's. It is a fully functional RESTful API to shorten long URLs, store them in a MySQL database, and provide redirect and analytics support.

---

## 🚀 Tech Stack

- Python 3
- Django 5
- Django REST Framework
- MySQL
- HTML (optional UI form)

---

## 📦 Project Features

- ✅ Create short URLs (random unique code)
- ✅ Retrieve original URL from short code
- ✅ Redirect from short code to original
- ✅ Update existing short URL
- ✅ Delete short URL
- ✅ Track number of visits (access count)
- ✅ View statistics (analytics)

---

## 🧪 API Endpoints

| Method | Endpoint                          | Description                      |
|--------|-----------------------------------|----------------------------------|
| POST   | `/shorten`                        | Create a new short URL           |
| GET    | `/shorten/<short_code>`           | Retrieve original URL            |
| PUT    | `/shorten/<short_code>/update`    | Update a short URL               |
| PATCH  | `/shorten/<short_code>/update`    | Partially update original URL    |
| DELETE | `/shorten/<short_code>/delete`    | Delete a short URL               |
| GET    | `/shorten/<short_code>/stats`     | View URL statistics              |
| GET    | `/s/<short_code>`                 | Redirect to original URL         |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Muhammad-Shiraz/muhammad-innovaxel-shiraz.git
cd muhammad-innovaxel-shiraz
```

2. Set up virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. MySQL Setup
  Create database shortener_db in MySQL
  Set your DB username and password in settings.py

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shortener_db',
        'USER': 'root',  # or your custom user
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server
```bash
python manage.py runserver
```

🧪 Testing API (via Postman)
Use Postman to test endpoints.

JSON payload example for creating a short URL:

```bash
{
  "original_url": "https://youtube.com"
}
```
Author: 
Muhammad Shiraz
Email: shirazshahzad876@gmail.com
GitHub: @Muhammad-Shiraz
