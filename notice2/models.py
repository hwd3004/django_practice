from django.db import models
from account.models import User

VISIBILITY_CHOICES = (
    ('공개', '공개'),
    ('비공개', '비공개')
)


class Notice2(models.Model):

    title = models.CharField(max_length=150)

    # https://yeko90.tistory.com/entry/django-기초-Foreign-Key외래키관계에서의-reversename-사용법
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)

    password = models.CharField(null=True, max_length=100, default=None)

    content = models.TextField()

    # attachment = models.FileField(null=True)

    watched = models.IntegerField(default=0)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notice2"


class Notice2_Attachment(models.Model):
    notice = models.ForeignKey(Notice2, on_delete=models.CASCADE)
    filename = models.CharField(null=True, max_length=300)
    path = models.CharField(null=True, max_length=300)
    attachment = models.FileField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notice2_attachment"
