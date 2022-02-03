from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from notice.forms import NoticeForm


def result(msg, status):
    return {
        'status': status,
        'msg': msg
    }


def list(request: HttpRequest):
    return render(request, 'notice_list.html')


def newpost(request: HttpRequest):

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)

        print(form)

        if form.is_valid():
            form.save()
            print("성공")
        else:
            print("실패")

        return JsonResponse(result("200", 1))
    else:
        form = NoticeForm()
        return render(request, 'notice_newpost.html', {'form': form})
