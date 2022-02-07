import re
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from account.models import User
from base.views import getSessionUserId, responseAjax
from notice.forms import NoticeCreationForm
from notice.models import Notice
from django.core.files.storage import FileSystemStorage


def list(request: HttpRequest):
    return render(request, 'notice_list.html')


def create(request: HttpRequest):

    if request.method == 'POST':
        try:
            form = NoticeCreationForm(request.POST, request.FILES)

            # print(form)

            if form.is_valid():
                temp_form: Notice = form.save(commit=False)

                reg = re.compile('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')
                regResult = reg.search(temp_form.title)
                if regResult != None:
                    return JsonResponse(responseAjax("제목에는 특수문자를 쓸 수 없습니다.", 3))

                temp_form.author = User.objects.filter(pk=getSessionUserId(request)).first()

                if temp_form.visibility == "private":
                    if temp_form.password == "" or temp_form.password == None:
                        return JsonResponse(responseAjax("비공개 체크시 비밀번호가 필요합니다.", 2))

                files = request.FILES.getlist('attachment')
                fileList = []
                if len(files) != 0:
                    for tempFile in files:
                        fs = FileSystemStorage(base_url="notice/")
                        tempFilePath = fs.save(f"notice/{tempFile.name}", tempFile)
                        fileList.append(tempFilePath)

                    temp_form.attachment = str(fileList)

                temp_form.save()
                return JsonResponse(responseAjax("등록 성공", 1))
            else:
                return JsonResponse(responseAjax("글 내용을 입력해주세요.", 0))
        except Exception as e:
            print(e)
            return JsonResponse(responseAjax("에러 발생", -1))

    else:
        form = NoticeCreationForm()
        return render(request, 'notice_create.html', {'form': form})
