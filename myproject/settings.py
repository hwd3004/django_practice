"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+slkn8dxezkpk-c0ml@5afy2^sj-gk0j+rq)s@t$sdvvkow5!w'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = []
# DEBUG = False
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'annoucement.apps.AnnoucementConfig',
    'notice.apps.NoticeConfig',
    'lab.apps.LabConfig',
    'notice2.apps.Notice2Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS에 베이스로 쓸 템플릿 경로 지정
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'practicedb',
        'USER': 'geist9',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# https://velog.io/@wbsl0427/Django-Static-파일-경로-설정-및-js와-html분리
# https://donis-note.medium.com/장고-스태틱파일에-대해서-알아보자-django-static-files-fcd271e89f96

# 각 static 파일에 대한 url prefix, 템플릿 태그 {% static “경로” %}에 의해 참조되는 설정, 항상 /로 끝나도록 설정해야 함.
STATIC_URL = 'static/'

STATIC_DIR = os.path.join(BASE_DIR, 'static')

# File System Loader에 의해 참조됨.
STATICFILES_DIRS = [
    STATIC_DIR,
]

#  python manage.py collectstatic 명령이 참조되는 설정, 여러 디렉토리로 나눠진 static 파일을 이 경로에 복사 (배포에서만 의미가 있습니다.)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 웹 URL을 통해 첨부파일에 접근할 수 있는 URL 경로
MEDIA_URL = 'media/'
# 실제 파일이 저장될 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 2.5MB 이상의 파일을 업로드하려면 장고 기본 변수의 수정이 필요하다
# https://docs.djangoproject.com/en/4.0/ref/settings/#file-upload-max-memory-size
# https://docs.djangoproject.com/en/4.0/ref/settings/#data-upload-max-memory-size
# 1GB
FILE_UPLOAD_MAX_MEMORY_SIZE = 1073741824
DATA_UPLOAD_MAX_MEMORY_SIZE = 1073741824
# FILE_UPLOAD_TEMP_DIR = 'tmp/'
# FILE_UPLOAD_PERMISSIONS = 0o755


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
