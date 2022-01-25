from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import context

from account.models import User


def signup(request: HttpRequest):
    if(request.method == 'POST'):
        userId = request.POST.get('userId')
        password = request.POST.get('password')

        newUser = User()

        newUser.userId = userId
        newUser.password = password

        # db에 인서트
        newUser.save()

        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login(request):
    context = {'data': 'data'}
    return render(request, 'login.html', context)
