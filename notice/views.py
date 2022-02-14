from datetime import datetime
import json
from pickle import FALSE
import re
from tokenize import Number
from django.http import FileResponse, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from account.models import User
from base.views import getSessionUserId, responseAjax
from notice.forms import NoticeCreationForm
from notice.models import Notice, Notice_Attachment
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models.fields.files import FieldFile
from django.db.models import Q


def search(request: HttpRequest):
    # temp = Notice.objects.filter(title__contains='fg')
    print('search 호출')
    return JsonResponse(0)


def detail(request: HttpRequest, pk):

    # print(pk)
    notice: Notice = get_object_or_404(Notice, pk=pk)
    # print(notice)

    # if notice.password != None:
    #     return render(request, 'notice_detail.html', {'password': notice.password})

    notice.watched += 1
    notice.save()

    # https://velog.io/@inyong_pang/Django-QuerySet
    # 장고 쿼리셋

    noticeAttach = Notice_Attachment.objects.filter(notice=notice).values()
    # print(noticeAttach)
    # <QuerySet [{'id': 13, 'notice_id': 60, 'path': 'media/notice/2022-02-08 16:11:22/화면 캡처 2022-02-04 105829.jpg', 'attachment': 'notice/2022-02-08 16:11:22/화면 캡처 2022-02-04 105829.jpg', 'createdAt': datetime.datetime(2022, 2, 8, 16, 11, 22, 571371), 'updatedAt': datetime.datetime(2022, 2, 8, 16, 11, 22, 571386)}, {'id': 14, 'notice_id': 60, 'path': 'media/notice/2022-02-08 16:11:22/주석 2022-01-25 111914.jpg', 'attachment': 'notice/2022-02-08 16:11:22/주석 2022-01-25 111914.jpg', 'createdAt': datetime.datetime(2022, 2, 8, 16, 11, 22, 573495), 'updatedAt': datetime.datetime(2022, 2, 8, 16, 11, 22, 573507)}]>

    attach = []
    for item in noticeAttach:
        path = item['path']
        filename = item['filename']
        id = item['id']
        attach.append({'filename': filename, 'path': path, 'id': id})

    # noticeAttach = Notice_Attachment.objects.filter(notice=notice).all()
    # <QuerySet [<Notice_Attachment: Notice_Attachment object (13)>, <Notice_Attachment: Notice_Attachment object (14)>]>

    if notice.visibility == 'private':
        print()

    return render(request, 'notice_detail.html', {'notice': notice, 'attach': attach})


def removeHasAttach(request: HttpRequest):
    try:
        if request.method == 'POST':
            hasAttachId: int = json.loads(request.body)['hasAttachId']

            item: Notice_Attachment = Notice_Attachment.objects.get(pk=hasAttachId)
            item.delete()

            return JsonResponse(responseAjax('첨부파일 삭제 완료', 1))
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return JsonResponse(responseAjax('에러 발생', 0))


def delete(request: HttpRequest, pk):
    try:
        print(f"pk : {pk}")
        notice: Notice = get_object_or_404(Notice, pk=pk)
        if getSessionUserId(request=request) != notice.author.pk:
            return JsonResponse(responseAjax('비정상적 접근', -1))
        else:
            notice.delete()

            return JsonResponse(responseAjax('삭제 완료', 1))
    except Exception as e:
        return JsonResponse(responseAjax('에러 발생', 0))


def update(request: HttpRequest, pk):
    notice: Notice = get_object_or_404(Notice, pk=pk)

    noticeAttach = Notice_Attachment.objects.filter(notice=notice).values()

    attach = []
    if noticeAttach != None:
        for item in noticeAttach:
            path = item['path']
            filename = item['filename']
            id = item['id']
            attach.append({'filename': filename, 'path': path, 'id': id})

    if request.method == 'POST':
        try:
            form = NoticeCreationForm(request.POST, request.FILES, instance=notice)

            if form.is_valid():
                temp_form: Notice = form.save(commit=False)

                if temp_form.author.pk != getSessionUserId(request=request):
                    return JsonResponse(responseAjax("비정상적 접근 : 글 작성자가 아닙니다.", 4))

                reg = re.compile('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')
                regResult = reg.search(temp_form.title)
                if regResult != None:
                    return JsonResponse(responseAjax("제목에는 특수문자를 쓸 수 없습니다.", 3))

                if temp_form.visibility == "private":
                    if temp_form.password == "" or temp_form.password == None:
                        return JsonResponse(responseAjax("비공개 체크시 비밀번호가 필요합니다.", 2))

                files = request.FILES.getlist('attachment')

                temp_form.save()

                noticeObj = Notice.objects.get(pk=pk)

                if len(files) != 0:
                    for tempFile in files:
                        fs = FileSystemStorage(base_url="notice/")
                        currentTime: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        tempFilePath = fs.save(f"notice/{currentTime}/{tempFile.name}", tempFile)

                        newNoticeAttach = Notice_Attachment()
                        newNoticeAttach.filename = tempFile.name
                        newNoticeAttach.notice = noticeObj
                        newNoticeAttach.path = f"media/{tempFilePath}"
                        newNoticeAttach.attachment = tempFilePath

                        newNoticeAttach.save()

                return JsonResponse(responseAjax("변경 완료", 1))
            else:
                return JsonResponse(responseAjax("form is invalid.", 5))
        except Exception as e:
            print(e)
            return render(request, responseAjax('에러 발생', -1))

    else:
        return render(request, 'notice_update.html', {'notice': notice, 'attach': attach})


def list(request: HttpRequest):

    searchType = request.GET.get('searchType')
    print(searchType)

    keyword = request.GET.get('keyword')
    print(keyword)

    if searchType == 'title':
        list = Notice.objects.order_by('-id').all().filter(title__contains=keyword)
        paginator = Paginator(list, 2)

        pageNumber = request.GET.get("page")

        if pageNumber is None:
            pageObj = paginator.get_page(1)

            return render(request, 'notice_list.html', {"pageObj": pageObj, 'searchType': searchType, 'keyword': keyword})

        else:
            pageObj = paginator.get_page(pageNumber)

            return render(request, 'notice_list.html', {"pageObj": pageObj, 'searchType': searchType, 'keyword': keyword})

    elif searchType == 'titleAndContent':
        list = Notice.objects.order_by('-id').all().filter(Q(title__contains=keyword) | Q(content__contains=keyword))
        paginator = Paginator(list, 2)

        pageNumber = request.GET.get("page")

        if pageNumber is None:
            pageObj = paginator.get_page(1)

            return render(request, 'notice_list.html', {"pageObj": pageObj, 'searchType': searchType, 'keyword': keyword})

        else:
            pageObj = paginator.get_page(pageNumber)

            return render(request, 'notice_list.html', {"pageObj": pageObj, 'searchType': searchType, 'keyword': keyword})

    # https://django-orm-cookbook-ko.readthedocs.io/en/latest/asc_or_desc.html
    # 역순 정렬
    list = Notice.objects.order_by('-id').all()
    paginator = Paginator(list, 2)

    pageNumber = request.GET.get("page")

    if pageNumber is None:
        pageObj = paginator.get_page(1)

        return render(request, 'notice_list.html', {"pageObj": pageObj})

    else:
        pageObj = paginator.get_page(pageNumber)

        return render(request, 'notice_list.html', {"pageObj": pageObj})


def create(request: HttpRequest):
    if request.method == "GET":
        print(getSessionUserId(request=(request)))

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
                print(files)

                # notice 테이블에 배열형태로 칼럼에 문자를 저장하기
                # if len(files) != 0:
                #     for tempFile in files:
                #         fs = FileSystemStorage(base_url="notice/")
                #         tempFilePath = fs.save(f"notice/{tempFile.name}", tempFile)
                #         fileList.append(tempFilePath)

                #     temp_form.attachment = str(fileList)

                # temp_form.save()

                temp_form.save()
                # print(temp_form.save())
                # None

                noticeObj = Notice.objects.last()
                # print(noticeObj)

                if len(files) != 0:
                    for tempFile in files:
                        fs = FileSystemStorage(base_url="notice/")
                        currentTime: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        tempFilePath = fs.save(f"notice/{currentTime}/{tempFile.name}", tempFile)

                        newNoticeAttach = Notice_Attachment()
                        newNoticeAttach.filename = tempFile.name
                        newNoticeAttach.notice = noticeObj
                        newNoticeAttach.path = f"media/{tempFilePath}"
                        newNoticeAttach.attachment = tempFilePath

                        newNoticeAttach.save()

                return JsonResponse(responseAjax("등록 성공", 1))
            else:
                return JsonResponse(responseAjax("글 내용을 입력해주세요.", 0))
        except Exception as e:
            print(e)
            return JsonResponse(responseAjax("에러 발생", -1))

    else:
        form = NoticeCreationForm()
        return render(request, 'notice_create.html', {'form': form})
