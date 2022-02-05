from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):

    if request.session.get('user') != None:
        print(request.session.get('user'))
        print(request.session.get('user')['id'])

    return render(request, 'base.html')
