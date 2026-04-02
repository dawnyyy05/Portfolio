# 🌟 Dawn Portfolio

A personal portfolio website built with **Django** — showcasing projects, skills, and profile information.

---

## 📸 Preview

> A clean, dynamic portfolio web app with media uploads and admin management.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 6.x
- **Database:** SQLite3
- **Frontend:** HTML, CSS (Django Templates)
- **Media:** Pillow (image handling)
- **Deployment:** PythonAnywhere

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dawnyyy05/Portfolio.git
cd Portfolio
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🚀 Deploying to PythonAnywhere

1. Upload or clone this repo to PythonAnywhere
2. Set up a virtual environment and install requirements
3. Configure the WSGI file to point to `portfolio_site.wsgi`
4. Add your domain to `ALLOWED_HOSTS` in `settings.py`
5. Set static and media file paths in the Web tab
6. Reload your web app

---

## 📁 Project Structure

```
Portfolio/
├── portfolio/          # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── portfolio_site/     # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/              # Uploaded media files
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Dawn** — [GitHub](https://github.com/dawnyyy05)
