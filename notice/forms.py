from django import forms
from django.db import models

from notice.models import Notice


class NoticeCreationForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'author', 'visibility', 'content', 'file']
        labels = {
            'title': '제목',
            'author': '작성자',
            'visibility': '공개여부',
            'content': '내용',
            'file': '첨부파일'
        }
