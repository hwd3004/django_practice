from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView
from account.models import User
from base.views import getSessionUserId, responseAjax

from lab.forms import LabCreationForm
from lab.models import Lab

from django.core.files.storage import FileSystemStorage


def labcreate(request: HttpRequest):
    if request.method == 'POST':
        try:
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
                fileList = []

                # print(files)
                # [<TemporaryUploadedFile: 파일명.파일확장자 (application/x-msdownload)>]

                # print(type(files))
                # <class 'list'>

                for tempFile in files:
                    fs = FileSystemStorage(base_url="lab/")
                    
                    print(f"1 : {tempFile}")
                    # 파일명.파일확장자
                    # print(type(tempFile))
                    # <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>
                    
                    print(f"2 : {tempFile.name}")
                    
                    tempFilePath = fs.save(f"lab/{tempFile.name}", tempFile)
                    print(f"3: {tempFilePath}")
                    # 경로/파일명.파일확장자
                    
                    fileList.append(tempFilePath)
                    
                    
                temp_lab.file = str(fileList)

                # form.save()
                temp_lab.save()

                return JsonResponse(responseAjax("등록 성공", 1))
            else:
                # print(form.errors)
                return JsonResponse(responseAjax("등록 실패", 0, form.errors))
        except Exception as e:
            print(e)
            return JsonResponse(responseAjax("에러 발생", -1,))
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
