from django.http import JsonResponse
from django.views import View
from users.models import User


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
