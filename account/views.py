import json
from django.shortcuts import redirect, render
from django.http import HttpRequest, JsonResponse, request

from account.models import User


def checkid(request: HttpRequest):
    # 아이디 중복확인
    if(request.method == 'POST'):

        data = json.loads(request.body)

        userId = data['userId']

        # 0 - 이미 있는 아이디, 1 - 없는 아이디, 사용 가능
        result = {
            'status': 0
        }

        try:
            checkExistId = User.objects.get(userId=userId)

            if checkExistId:
                return JsonResponse(result)

        except User.DoesNotExist:
            result['status'] = 1
            return JsonResponse(result)

        return 0
    else:
        return redirect('/')


def signup(request: HttpRequest):

    if(request.method == 'POST'):
        data = json.loads(request.body)

        # https://my-devblog.tistory.com/28
        # json과 dict 간에 서로 변환 방법

        # https://link2me.tistory.com/2103
        # https://link2me.tistory.com/2108
        # django와 ajax 활용

        # userId = data['userId']
        # password = data['password']

        # 0 - 이미 있는 아이디, 1 - 없는 아디, 회원가입 진행
        # 2 - 이미 있는 이메일, 3 - 이미 있는 휴대전화번호
        result = {
            'status': 0
        }

        try:
            checkExistId = User.objects.get(userId=data['userId'])
            checkExistEmail = User.objects.get(email=data['email'])
            checkExistMobilePhoneNumber = User.objects.get(
                mobilePhoneNumber=data['mobilePhoneNumber'])

            if checkExistId:
                result['status'] = 0
                return JsonResponse(result)

            elif checkExistEmail:
                result['status'] = 2
                return JsonResponse(result)

            elif checkExistMobilePhoneNumber:
                result['status'] = 3
                return JsonResponse(result)

        except User.DoesNotExist:
            newUser = User()

            newUser.userId = data['userId']
            newUser.password = data['password']
            newUser.username = data['username']
            newUser.department = data['department']
            newUser.position = data['position']
            newUser.email = data['email']
            newUser.phoneNumber = data['phoneNumber']
            newUser.mobilePhoneNumber = data['mobilePhoneNumber']

            newUser.save()

            result['status'] = 1

            # ajax 사용시 JsonResponse를 리턴해야함
            return JsonResponse(result)

    else:
        return render(request, 'signup.html')


def login(request: HttpRequest):
    if(request.method == 'POST'):

        data = json.loads(request.body)

        userId = data['userId']
        password = data['password']

        result = {
            'status': 0
        }

        try:
            checkExistId: User = User.objects.filter(
                userId=userId).filter(password=password).first()

            # print("===============")
            # print("checkExistId")
            # print(checkExistId)
            # print(checkExistId.id)
            # print(type(checkExistId.id))
            # print(type(checkExistId.userId))
            # print(type(checkExistId.pk))
            # print("===============")

            if checkExistId:

                sessionUser = {
                    'id': checkExistId.pk,
                    'userId': checkExistId.userId
                }

                request.session['user'] = sessionUser

                result['status'] = 1

                return JsonResponse(result)
            else:
                return JsonResponse(result)

        except User.DoesNotExist:
            return JsonResponse(result)
    else:
        return render(request, 'login.html')


def logout(request: HttpRequest):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')


def findid(request: HttpRequest):
    if request.method == 'POST':
        return 0
    else:
        return render(request, 'findid.html')
