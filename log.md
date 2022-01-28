sudo service mysql start

```
git add .
git commit -m ""
git push
```

python manage.py makemigrations

python manage.py migrate

===

테이블 새로 만들기

```
python manage.py showmigrations

python manage.py migrate --fake 테이블이름 zero

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

python manage.py makemigrations

python manage.py migrate
```

===