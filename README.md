Project Name: Hands-On Assignment 3: Create a Simple Q&A Chatbot with Python
Author: Ronit Rajesh Pawar

Dependencies:
- django
- chatterbot
- chatterbot_corpus

Instructions for setup in Windows:
1. Open WSL terminal
2. Create virtual environment using commands below
    - python -m venv venv
    - source venv/bin/activate
3. Now virtual env is created install dependencies using pip.
    - pip install django chatterbot chatterbot_corpus
4. Setup Django project
    - django-admin startproject chatbot_project
    - cd chatbot_project
    - python manage.py startapp chatbot_app
5. Create CLI command to run chatbot
    - nano chatbot_app/management/commands/chat.py
6. Add 'chatbot_app' to INSTALLED_APPS in chatbot_project/settings.py
7. Run chatbot via `python manage.py chat`
