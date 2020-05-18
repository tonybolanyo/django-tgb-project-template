#!/bin/sh

cwd=$(pwd)

cd /app/src

coverage run --source='.' --rcfile=.coveragerc manage.py test --failfast --settings={{ project_name }}.settings.test
coverage html -d htmlcov
coverage report -m

cd $cwd