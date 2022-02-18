from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from account.models import User
from base.views import getSessionUserId, responseAjax

from notice2.forms import Notice2CreationForm
from notice2.models import Notice2
from django.core.paginator import Paginator


def getList(request: HttpRequest):

    return JsonResponse(responseAjax("asdsad", 1))


def list(request: HttpRequest):
    return render(request, 'notice2_list.html')


def create(request: HttpRequest):
    if request.method == 'POST':
        form = Notice2CreationForm(request.POST, request.FILES)

        print(form)

        if form.is_valid():
            temp_form: Notice2 = form.save(commit=False)

            temp_form.author = User.objects.filter(pk=getSessionUserId(request)).first()

            temp_form.save()

            return JsonResponse(responseAjax("등록 완료", 1))
        else:
            return JsonResponse(responseAjax("등록 실패", 0))
    if request.method == 'GET':
        return render(request, 'notice2_create.html')
