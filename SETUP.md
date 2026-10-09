# Sunrise Catering Services - Setup

This project uses Django and SQLite.

## 1. Open the project

Open the `catering service` folder in VS Code.

## 2. Create/activate a virtual environment

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Django

```bash
pip install -r requirements.txt
```

## 4. Create the database

```bash
python manage.py migrate
python manage.py seed_demo
```

## 5. Create an admin account

```bash
python manage.py createsuperuser
```

## 6. Start the website

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## Main demo flow

1. Open Home.
2. Explore Services, Menu, Packages and Gallery.
3. Create an account.
4. Log in.
5. Click Book Now.
6. Submit an event booking.
7. Open the booking details.
8. Open Django Admin and show that the booking, payment record and contact enquiries are stored in SQLite.

The payment section is intentionally a demonstration record only; it does not process real money.
