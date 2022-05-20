# from django.http import JsonResponse
#
#
# def login_status(func):
#     def inner(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return func(request,*args,**kwargs)
#         else:
#             return JsonResponse({
#                 'code':400,
#                 'errmsg':'请先登录'
#             })
#     return inner
#
#
