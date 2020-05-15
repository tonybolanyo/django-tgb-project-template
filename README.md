# django-tgb-project-template

Basic Django project template to start a project as soon as possible

## Usage

```
pyenv virtualenv {{ project_name }}
pyenv activate {{ project_name }}
pip install django
django-admin startproject --template https://github.com/tonybolanyo/django-tgb-project-template/archive/master.zip -e py,yml,yaml,md,sh,env.sample {{ project_name }}
cd {{ project_name }}
cp docker/django.env.sample docker/django.env
cp docker/pgadmin.env.sample docker/pgadmin.env
cp docker/postgres.env.sample docker/postgres.env
docker-compose up
```
