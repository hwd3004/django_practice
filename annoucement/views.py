import re
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View

from base.views import result


def list(request: HttpRequest):

    return render(request, 'list.html')


def newpost(request: HttpRequest):
    if(request.method == 'POST'):
        print(request.POST)
        # print(request.POST.get("title"))
        print(request.FILES)

        data: dict = {}

        # for i in request.POST:
        #     print(request.POST[i])
        # data[i] = request.POST[i]

        # for i in data:
        #     print(data[i])

        # print(data.get('title'))

        print(request.POST.get("title"))

        return JsonResponse(result("공지 등록 완료", 1))
    else:
        return render(request, 'newpost.html')


class NewPost(View):
    def post(self, request: HttpRequest):
        print("NewPost 클래스 호출")
        # print(request.POST)
        print(self.request)
        print(request.POST.get("title"))
        # print(request.POST.get("title"))
        return JsonResponse(result("공지 등록 완료", 1))
