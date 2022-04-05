https://iamiet.tistory.com/54?category=928115 - django Ubuntu 에서 mysqlclient 설치오류 해결방법

sudo apt install python3-dev default-libmysqlclient-dev build-essential

---

sudo service mysql start

```
git add . && git commit -m "" && git push
```

python3 manage.py makemigrations && python3 manage.py migrate

python3 manage.py runserver

rm -rf media && mkdir media

---

python manage.py makemigrations

python manage.py migrate

---

테이블 새로 만들기

```
python manage.py showmigrations

python manage.py migrate --fake 테이블이름 zero

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

python manage.py makemigrations

python manage.py migrate
```

---

파일 업로드

https://2ham-s.tistory.com/307 - formdata 설명

https://inpa.tistory.com/136 - formdata 설명

구글 - formdata ajax

https://truecode-95.tistory.com/167 - formdata로 json 파라미터 넘기기

https://eveningdev.tistory.com/47 - django 파일 업로드

https://bcdragonfly.tistory.com/18 - django 파일 여러개 업로드

---

https://wikidocs.net/70855

https://junlab.tistory.com/193

https://076923.github.io/posts/Python-Django-11/

https://yeko90.tistory.com/entry/django-기초-Foreign-Key외래키관계에서의-reversename-사용법

https://roseline124.github.io/django/2019/04/10/pickmeal-reviewform.html

구글 - django 파일 업로드 "form.is_valid"

https://cjh5414.github.io/django-file-upload/

---

https://www.reddit.com/r/django/comments/kxla55/django_ajax_jquery_and_formdata/

https://learnbatta.com/blog/django-image-and-file-upload-using-ajax-21/

구글 - django modelform

https://wayhome25.github.io/django/2017/05/06/django-model-form/

---

https://microsoft.tistory.com/995

vscode 파이썬 max-line 설정

---

https://velog.io/@polynomeer/배열을-데이터베이스에-저장하는-방법

---

https://myhappyman.tistory.com/178 - jQuery - ajax xhr을 활용한 파일 업로드 진행 상태 확인하기

https://youtu.be/osqkFdIyDNg - Python Django Multiple File Upload Using Ajax With Progress Bar | JavaScript File Upload Progressbar

---

https://94incheon.github.io/django/Django_DateFomat/ - Django : 장고 DTL 언어 - 날짜(Date) 출력, 저장하기

https://youngwonhan-family.tistory.com/39 - 4. 게시판 만들기 - Django 템플릿 & 페이징(Pagination) 처리( feat. GIF )

https://eveningdev.tistory.com/26 - [django] 페이지 구현(Page), 페이징 처리(Pagination)

https://ysyblog.tistory.com/44 - [Django] 게임 목록(검색, 필터, 가격필터 기능 및 페이징 기능 구현 그리고 최저가 기능 구현)

---

https://velog.io/@inyong_pang/Django-QuerySet - 장고 쿼리셋

---

https://youtu.be/MpDZ34mEJ5Y - How to Upload and Download file with django

https://parkhyeonchae.github.io/ - 장고 crud 정리 블로그

---

https://parkhyeonchae.github.io/2020/04/11/django-project-23/ - 글 수정

---

https://wikidocs.net/71806 - 장고 3-15 검색과 정렬

http://shopnilsazal.github.io/django-pagination-with-basic-search/ - Django Pagination with Basic Search