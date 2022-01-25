from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.userId

    # return을 그냥 self로 하면 User.objects.get 같은 함수들이 작동하지 않는다
    # def __str__(self):
    #     return self
