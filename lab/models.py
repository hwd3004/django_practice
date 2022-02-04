from django.db import models

from account.models import User


class Lab(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='lab', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='image/', null=False)
    file = models.FileField(upload_to='file/', null=True)
    content = models.TextField(null=True)

    createdAt = models.DateField(auto_now_add=True, null=True)
