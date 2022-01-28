from django.http import HttpRequest
from django.shortcuts import render


def list(request: HttpRequest):

    return render(request, 'list.html')
