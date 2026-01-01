# Drop Me – Live RVM Status & Discovery API

This project implements Task 2 of the Drop Me Backend Internship challenge using *Django* 

The API helps users and technicians discover *active Recycling Vending Machines (RVMs)* and view machines that have been used recently, with clean responses, efficient querying, and timezone-aware logic.

---

## Features
- RVM data model including:
  - location
  - status (active / inactive)
  - last usage timestamp
- Endpoint to list *active RVMs only*
- Results ordered by *most recent activity*
- Optional filtering:
  - by location (case-insensitive)
  - by recent usage within a configurable number of hours (e.g., last 24 hours)
- Timezone-aware datetime handling
- Clean and minimal API responses

---

## Tech 
- Python 3.10+
- Django
- Django REST Framework
- SQLite (for local development)

---

## Setup Instructions (Windows)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

