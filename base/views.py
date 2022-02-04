from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):

    print(request.session.get('user'))
    print(request.session.get('user')['id'])

    return render(request, 'base.html')
