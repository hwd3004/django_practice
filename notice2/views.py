from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from notice2.forms import Notice2CreationForm


def list(request: HttpRequest):
    return render(request, 'notice2_list.html')


def create(request: HttpRequest):
    if request.method == 'POST':
        form = Notice2CreationForm(request.POST, request.FILES)
        
        print(form.is_multipart())

        return JsonResponse({'asd': 'asd'})
    if request.method == 'GET':
        return render(request, 'notice2_create.html')
