from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):

    print(request.session.get('user'))

    return render(request, 'base.html')
