from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    # 성명
    username = models.CharField(max_length=50)

    # 부서
    department = models.CharField(max_length=200)

    # 직책 및 직급
    position = models.CharField(max_length=200)

    email = models.CharField(max_length=50, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # 일반전화
    phoneNumber = models.CharField(max_length=20, null=True)

    # 휴대전화
    mobilePhoneNumber = models.CharField(max_length=20, unique=True)

    # def __str__(self):
    #     return self.userId

    # return을 그냥 self로 하면 User.objects.get 같은 함수들이 작동하지 않는다
    # def __str__(self):
    #     return self
