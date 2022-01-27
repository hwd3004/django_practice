import email
import json
from django.shortcuts import redirect, render
from django.http import HttpRequest, JsonResponse
from account.models import User


def checkExistId(userId):
    try:
        User.objects.get(userId=userId)
        return True
    except User.DoesNotExist:
        return False


def checkExistEmail(email):
    try:
        User.objects.get(email=email)
        return True
    except User.DoesNotExist:
        return False


def checkExistMobilePhoneNumber(MobilePhoneNumber):
    try:
        User.objects.get(MobilePhoneNumber=MobilePhoneNumber)
        return True
    except User.DoesNotExist:
        return False


def result(msg, status):
    return {
        'status': status,
        'msg': msg
    }


def checkid(request: HttpRequest):
    # 아이디 중복확인
    if(request.method == 'POST'):

        data = json.loads(request.body)

        if checkExistId(data['userId']):
            return JsonResponse(result("이미 있는 아이디입니다.", 0))
        else:
            return JsonResponse(result("사용 가능한 아이디입니다.", 1))
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

        # result
        # -1 가입 실패
        # 0 - 이미 있는 아이디, 1 - 없는 아디, 회원가입 진행
        # 2 - 이미 있는 이메일, 3 - 이미 있는 휴대전화번호

        try:
            # https://velog.io/@khh180cm/filter와-get의-차이장고
            # https://hyun0k.tistory.com/entry/Project-Westagram-1

            if User.objects.filter(userId=data['userId']).exists():
                return JsonResponse(result('이미 있는 아이디입니다.', 0))

            elif User.objects.filter(email=data['email']).exists():
                return JsonResponse(result('이미 있는 이메일입니다.', 2))

            elif User.objects.filter(mobilePhoneNumber=data['mobilePhoneNumber']).exists():
                return JsonResponse(result('이미 있는 휴대전화번호입니다.', 3))

            else:
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

                return JsonResponse(result("가입이 완료되었습니다.", 1))
        except:
            return JsonResponse(result("가입에 실패하였습니다.", -1))

    else:
        return render(request, 'signup.html')


def login(request: HttpRequest):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)

            checkExistId: User = User.objects.filter(
                userId=data['userId']).filter(password=data['password']).first()

            if(checkExistId):
                sessionUser = {
                    'id': checkExistId.pk,
                    'userId': checkExistId.userId,
                    'username': checkExistId.username
                }

                request.session['user'] = sessionUser

                return JsonResponse(result("로그인 완료", 1))
            else:
                return JsonResponse(result("아이디와 비밀번호를 확인하여주세요.", 0))

        except:
            return JsonResponse(result("Exception : 로그인 실패", -1))
    else:
        return render(request, 'login.html')


def logout(request: HttpRequest):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')


def findid(request: HttpRequest):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            reqType = data['reqType']
            username = data['username']
            email = data['email']

            if reqType == 'findid':
                findUserId: User = User.objects.filter(
                    username=username).filter(email=email).first()

                if findUserId:
                    return JsonResponse(result(f"찾은 아이디 : {findUserId.userId}", 1))
                else:
                    return JsonResponse(result("아이디가 없습니다.", 0))

            elif reqType == 'findpassword':
                userId = data['userId']

                findPassword: User = User.objects.filter(userId=userId).filter(
                    username=username).filter(email=email).first()

                if findPassword:
                    return JsonResponse(result(f"찾은 비밀번호 : {findPassword.password}", 1))
                else:
                    return JsonResponse(result("비밀번호를 찾지 못했습니다. 입력란을 확인하여주세요.", 0))
        except:
            return JsonResponse(result("에러 : 계정 찾기 실패.", -1))
    else:
        return render(request, 'findid.html')
