from django.urls import re_path
from users.views import *

urlpatterns = {
    # 判断用户名是否重复
    re_path('^usernames/(?P<username>\w{5,20})/count/$', UsernameCountView.as_view()),
    re_path('^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', MobileCountView.as_view()),
}
