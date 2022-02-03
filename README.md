# Warehouse Inventory System 2022

Developer: Gen Deu L. Gagarin

Freelance Project started on Feb. 3, 2022 for
Hardware-Business owned by Grace Ico.

Email for inquiries: gendeulgagarin@gmail.com



////////////////////////////////////////////
$ mkdir WIS-2022-project
$ cd WIS-2022-project/
$ python3 -m venv venv --prompt WIS-2022-project
$ tree -L 2
$ ls venv/bin/ | grep activate
$ source venv/bin/activate
$ which python
$ which pip
$ python -m pip install django==3.2.7
$ python -m pip install --upgrade pip
$ pip list
$ pip freeze > requirements.txt
$ django-admin startproject WIS-2022 .
$ ls -l
$ python manage.py migrate
$ sqlite3 db.sqlite3
sqlite> .tables
$ python manage.py createsuperuser
$ python manage.py runserver