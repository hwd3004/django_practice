from urllib import request
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView
from account.models import User
from base.views import getSessionUserId, result

from lab.forms import LabCreationForm
from lab.models import Lab


def labcreate(request: HttpRequest):
    if request.method == 'POST':
        form = LabCreationForm(request.POST, request.FILES)
        # print(form)
        # print(type(form))
        # <class 'lab.forms.LabCreationForm'>

        if form.is_valid():
            # print(form.cleaned_data['author'])
            # User object (1)

            # print(type(form.cleaned_data['author']))
            # <class 'account.models.User'>

            # print(User.objects.filter(pk=request.session.get('user')['id']).first())
            # User object (1)

            # print(type(User.objects.filter(
            #     pk=request.session.get('user')['id']).first()))

            # form.cleaned_data['author'] = User.objects.filter(
            #     pk=request.session.get('user')['id']).first()
            # 변경 불가 속성

            temp_lab: Lab = form.save(commit=False)
            temp_lab.author = User.objects.filter(pk=getSessionUserId(request)).first()

            # print(temp_lab)
            # Lab object (None)

            # print(type(temp_lab))
            # <class 'lab.models.Lab'>

            files = request.FILES.getlist('file')
            list = []
            print(files)
            print(type(files))
            i = 0
            for file in files:
                print(file)
                print(type(file))
                temp = {
                    'id': i,
                    'file': 'asd'
                }
                
            
            # form.save()
            temp_lab.save()

            return JsonResponse(result("등록 성공", 1))
        else:
            # print(form.errors)
            return JsonResponse(result("등록 실패", 0, form.errors))
    else:
        if getSessionUserId(request) == None:
            return redirect('/account/login')

        form = LabCreationForm()
        return render(request, 'labcreate.html', {'form': form})


class LabCreateView(CreateView):
    model = Lab

    form_class = LabCreationForm

    template_name = 'lab/templates/create.html'

    def form_valid(self, form):
        temp_lab: Lab = form.save(commit=False)

        request = HttpRequest

        temp_lab.author = User.objects.filter(pk=getSessionUserId(request)).first()
        temp_lab.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('')
