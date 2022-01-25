import json
from django.shortcuts import redirect, render
from django.http import HttpRequest, JsonResponse

from account.models import User


def signup(request: HttpRequest):

    if(request.method == 'POST'):
        data = json.loads(request.body)

        # https://my-devblog.tistory.com/28
        # json과 dict 간에 서로 변환 방법

        # https://link2me.tistory.com/2103
        # https://link2me.tistory.com/2108
        # django와 ajax 활용

        userId = data['userId']
        password = data['password']

        # 0 - 이미 있는 아이디, 1 - 없는 아디, 회원가입 진행
        result = {
            'status': 0
        }

        try:
            checkExistId = User.objects.get(userId=userId)

            if checkExistId:
                return JsonResponse(result)

        except User.DoesNotExist:
            newUser = User()

            newUser.userId = userId
            newUser.password = password
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

        except User.DoesNotExist:
            return JsonResponse(result)
    else:
        return render(request, 'login.html')


def logout(request: HttpRequest):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')
