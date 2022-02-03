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

파일 업로드

https://2ham-s.tistory.com/307 - formdata 설명

https://inpa.tistory.com/136 - formdata 설명

구글 - formdata ajax

https://truecode-95.tistory.com/167 - formdata로 json 파라미터 넘기기

https://eveningdev.tistory.com/47 - django 파일 업로드

https://bcdragonfly.tistory.com/18 - django 파일 여러개 업로드

===

https://wikidocs.net/70855

https://junlab.tistory.com/193

https://076923.github.io/posts/Python-Django-11/

https://yeko90.tistory.com/entry/django-기초-Foreign-Key외래키관계에서의-reversename-사용법

https://roseline124.github.io/django/2019/04/10/pickmeal-reviewform.html

구글 - django 파일 업로드 "form.is_valid"

https://cjh5414.github.io/django-file-upload/