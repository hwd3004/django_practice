from django.shortcuts import redirect, render
from django.http import HttpRequest


def result(msg: str, status: int, errors=None):
    return {
        'status': status,
        'msg': msg,
        'errors': errors
    }


def getSessionUserId(request: HttpRequest):

    if request.session.get('user') != None:
        pk: int = request.session.get('user')['id']
        return pk
    else:
        return None


def index(request: HttpRequest):

    # if request.session.get('user') != None:
    #     print(request.session.get('user'))
    #     print(request.session.get('user')['id'])

    return render(request, 'base.html')
