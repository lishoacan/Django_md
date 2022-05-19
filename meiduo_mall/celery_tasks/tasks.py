from ronglian_sms_sdk import SmsSDK

from celery_tasks.main import celery_app


@celery_app.task(name='smssdk_send_sms_code')
def smssdk_send_sms_code(mobile, sms_code):
    # 短信发送
    sdk = SmsSDK('8a216da8738dc94201738e5e40c000b1', '7b6e2a63d7d547eaaa8c3dcd5c39326e',
                 '8a216da8738dc94201738e5e419e00b8')
    result = sdk.sendMessage(tid='1', mobile=mobile, datas=(int(sms_code), 5))
    return result
