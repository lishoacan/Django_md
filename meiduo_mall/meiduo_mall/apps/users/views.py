from django.http import JsonResponse
from django.views import View
from users.models import User
import json, re
from django_redis import get_redis_connection
from django.contrib.auth import login


class UsernameCountView(View):
    def get(self, request, username):
        try:
            count = User.objects.filter(username=username).count()
        except Exception as e:
            return JsonResponse({
                'code': 400,
                'errmsg': '访问数据库失败',
            })
        return JsonResponse({
            'code': 200,
            'errmsg': 'OK',
            'count': count
        })


class MobileCountView(View):
    def get(self, request, mobile):
        try:
            count = User.objects.filter(mobile=mobile).count()
            return JsonResponse({
                'code': 200,
                'errmsg': 'OK',
                'count': count
            })
        except Exception as e:

            return JsonResponse({
                'code': 400,
                'errmsg': '数据库查询失败',
            })


class RegisterView(View):
    def post(self, request):
        dict = json.loads(request.body.decode())
        username = dict.get('username')
        password = dict.get('password')
        password2 = dict.get('password2')
        mobile = dict.get('mobile')
        sms_code = dict.get('sms_code')
        allow = dict.get('allow')
        if not all([username, password, password2, mobile, sms_code, allow]):
            return JsonResponse({
                'code': 400,
                'errmsg': '缺少必要参数'
            })
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return JsonResponse({
                'code': 400,
                'errmsg': 'username格式错误'
            })
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return JsonResponse({
                'code': 400,
                'errmsg': 'password格式有误'
            })
        if password != password2:
            return JsonResponse({
                'code': 400,
                'errmsg': 'password两次输入不一致'
            })
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return JsonResponse({
                'code': 400,
                'errmsg': 'mobile格式错误'
            })
        if allow != True:
            return JsonResponse({
                'code': 400,
                'errmsg': 'allow格式错误'
            })
        redis_client = get_redis_connection('verify_code')
        redis_sms_code = redis_client.get('sms_%s' % mobile)
        if not redis_sms_code:
            return JsonResponse({
                'code': 400,
                'errmsg': '短信验证码过期'
            })
        print(type(sms_code))
        print(type(redis_sms_code.decode()))
        print(sms_code)
        print(redis_sms_code.decode())
        if sms_code != redis_sms_code.decode():
            return JsonResponse({
                'code': 400,
                'errmsg': '短信验证码有误'
            })
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except Exception as e:
            return JsonResponse({
                'code': 400,
                'errmsg': '保存数据库出错'
            })
        login(request, user)

        response = JsonResponse({
            'code': 0,
            'errmsg': 'OK'
        })
        response.set_cookie('username',username,max_age=3600*24*14)
        return response
