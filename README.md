# Admission-Help-System
Gathering announcements, tips, links to study material and news stories about admissions into premier professional institutions (Engineering, Medicine, architecture, design ...)
## Setup Instructions
$ cd src/
$ make init
$ cd eduhelp/
$ pipenv run python manage.py migrate
$ pipenv run python manage.py createsuperuser
$ pipenv run python manage.py loaddata eduhelp/fixtures/*
$ pipenv run python manage.py runserver
