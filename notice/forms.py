from importlib.metadata import requires
from pickle import FALSE
from django import forms
from django.db import models

from notice.models import Notice


class NoticeCreationForm(forms.ModelForm):
    password = forms.CharField(required=False)
    attachment = forms.FileField(required=False)

    class Meta:
        model = Notice
        fields = ['title', 'visibility', 'password', 'content', 'attachment']
        labels = {
            'title': '제목',
            'password': '비밀번호',
            'visibility': '공개여부',
            'content': '내용',
            'attachment': '첨부파일',
        }
