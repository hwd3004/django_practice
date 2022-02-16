from importlib.metadata import requires
from pickle import FALSE
from django import forms

from notice2.models import Notice2




class Notice2CreationForm(forms.ModelForm):
    password = forms.CharField(required=False)
    attachment = forms.FileField(required=False)

    class Meta:
        model = Notice2
        fields = ['title', 'visibility', 'password', 'content', 'attachment']
        labels = {
            'title': '제목',
            'password': '비밀번호',
            'visibility': '공개여부',
            'content': '내용',
            'attachment': '첨부파일',
        }
