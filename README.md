# Admission-Help-System
Gathering announcements, tips, links to study material and news stories about admissions into premier professional institutions (Engineering, Medicine, architecture, design ...)
## Setup Instructions
1. cd src/
2. make init
3. cd eduhelp/
4. pipenv run python manage.py migrate
5. pipenv run python manage.py createsuperuser
6. pipenv run python manage.py loaddata eduhelp/fixtures/*
7. pipenv run python manage.py runserver
