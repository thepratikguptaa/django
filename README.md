# What is Django?
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

Django is a full-featured web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a set of tools and libraries for building web applications, including an ORM, a templating engine, and a built-in admin interface.

# Environment Setup
To get started with Django, you’ll need to install Python and create a virtual environment. You can create a virtual environment using the following commands:

```bash
# Windows
python -m venv .venv
```

```bash
# Linux/MacOS
python3 -m venv .venv
```
But for this time, I used [uv](https://docs.astral.sh/uv/) to manage virtual environment and other tools. It’s ridiculously easy and fast and cross-platform.

![UV logo](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310#only-dark)

## Installing Django
Now that you have a virtual environment set up, you can install Django using the following command:
```bash
uv pip install django
```
## Creating a Django Project
To create a Django project, you can use the following command:
```bash
django-admin startproject ProjectOne
```
```base
cd ProjectOne
```
## Running a Django development server
To start a Django development server, you can use the following command:
```bash
python manage.py runserver
```

---

🎉 **Happy Experimenting!** 🎉


*May your bugs be few and your features many!*