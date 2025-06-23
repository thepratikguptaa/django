### LinkedIn Post
[![LinkedIn Post](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/posts/thepratikguptaa_django-python-webdevelopment-activity-7342960914108760065-N7Tr?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFNTblUBnfiK5ntkG3s1-NXJ0TPqdRrZrz0)

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

## Project Structure
```
└── 📁django
    └── 📁.vscode
        └── settings.json
    └── 📁ProjectOne
        └── 📁batman
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-313.pyc
                └── admin.cpython-313.pyc
                └── apps.cpython-313.pyc
                └── forms.cpython-313.pyc
                └── models.cpython-313.pyc
                └── urls.cpython-313.pyc
                └── views.cpython-313.pyc
            └── admin.py
            └── apps.py
            └── forms.py
            └── 📁migrations
                └── __init__.py
                └── 📁__pycache__
                    └── __init__.cpython-313.pyc
                    └── 0001_initial.cpython-313.pyc
                    └── 0002_savegotham_description.cpython-313.pyc
                    └── 0003_alter_savegotham_type.cpython-313.pyc
                    └── 0004_candidatereviews_specialability_villainalliances.cpython-313.pyc
                    └── 0005_rename_villains_villainalliances_hero_and_more.cpython-313.pyc
                    └── 0006_rename_hero_villainalliances_heros.cpython-313.pyc
                    └── 0007_heroesalliances_delete_villainalliances.cpython-313.pyc
                    └── 0008_rename_candidatereviews_candidatereview_and_more.cpython-313.pyc
                └── 0001_initial.py
                └── 0002_savegotham_description.py
                └── 0003_alter_savegotham_type.py
                └── 0004_candidatereviews_specialability_villainalliances.py
                └── 0005_rename_villains_villainalliances_hero_and_more.py
                └── 0006_rename_hero_villainalliances_heros.py
                └── 0007_heroesalliances_delete_villainalliances.py
                └── 0008_rename_candidatereviews_candidatereview_and_more.py
            └── models.py
            └── 📁templates
                └── 📁batman
                    └── im_batman.html
                    └── villains.html
                    └── weapon_details.html
            └── tests.py
            └── urls.py
            └── views.py
        └── db.sqlite3
        └── manage.py
        └── 📁media
            └── 📁save-gotham
                └── alfred_pennyworth_gJM3LhW.png
                └── alfred_pennyworth_NJRxiy4.png
                └── alfred_pennyworth.png
                └── bruce_wayne.png
                └── elon_musk_14Lb2aH.png
                └── elon_musk_9TurQhc.png
                └── elon_musk_hLvBVk7.png
                └── elon_musk.png
                └── github_shipit.png
        └── 📁ProjectOne
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-313.pyc
                └── settings.cpython-313.pyc
                └── urls.cpython-313.pyc
                └── views.cpython-313.pyc
                └── wsgi.cpython-313.pyc
            └── asgi.py
            └── settings.py
            └── urls.py
            └── views.py
            └── wsgi.py
        └── 📁static
            └── style.css
        └── 📁templates
            └── layout.html
            └── 📁website
                └── index.html
        └── 📁theme
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-313.pyc
                └── apps.cpython-313.pyc
            └── apps.py
            └── 📁static
            └── 📁static_src
                └── .gitignore
                └── package-lock.json
                └── package.json
                └── postcss.config.js
                └── 📁src
                    └── styles.css
                └── 📁css
            └── 📁templates
                └── base.html
    └── README.md
```