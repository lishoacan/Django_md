# from ronglian_sms_sdk import SmsSDK
#
#
# def send():
#     sdk = SmsSDK('8a216da8738dc94201738e5e40c000b1', '7b6e2a63d7d547eaaa8c3dcd5c39326e',
#                  '8a216da8738dc94201738e5e419e00b8')
#     mobile = '15622281369'
#     codes = (666666,5)
#     resp = sdk.sendMessage(tid='1', mobile=mobile, datas=codes)
#     print(resp)
#
#
# if __name__ == '__main__':
#     send()
import random

code = int('%06d' % random.randint(0, 999999))
s_code = (code,5)
sms_code = (int('%06d' % random.randint(0, 999999)),5)
print(code)
print(type(code))
print(s_code)
print(type(s_code))
print(sms_code)
print(type(sms_code))