#!/bin/sh 

echo "==> Migration 파일 생성"
yes | python manage.py makemigrations --settings=todolist.settings.prod

echo "==> Migrate 실행"
python manage.py migrate --settings=todolist.settings.prod --fake-initial

echo "==> collectstatic 실행"
python manage.py collectstatic --settings=todolist.settings.prod --noinput -v 3

echo "==> 패키지 다운로드"
pip install -r /code/requirements.txt

echo "==> 배포!"
gunicorn todolist.wsgi:application -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE='todolist.settings.prod'