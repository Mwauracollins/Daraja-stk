import os

from mpesa.api.mpesa_express import MpesaExpress

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
shortcode = os.getenv("SHORTCODE")
passkey = os.getenv("PASSKEY")
call_back_url = os.getenv("CALLBACK_URL")

mpesa = MpesaExpress(
    env="sandbox",
    app_key=consumer_key,
    app_secret=consumer_secret,
    sandbox_url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
    live_url="https://safaricom.co.ke"
)

phone_number = "PHONE_NUMBER"
amount = 1
reference_code = "REFERENCE_CODE"

response = mpesa.stk_push(
    business_shortcode=shortcode,
    passcode=passkey,
    amount=amount,
    callback_url=call_back_url,
    reference_code=reference_code,
    phone_number=phone_number,
    description="Test payment"
)
print(response)

"""
FOR USE IN DJANGO FRAMEWORK YOU CAN USE A CLASS VIEW LIKE THIS:
"""
# pip install django-mpesa
# view.py
from django.views import View
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

class MpesaSTKPush(View):
    def get(self, request):
        client = MpesaClient()
        phone_number = "PHONE_NUMBER"
        amount = 1
        reference_code = "REFERENCE_CODE"
        call_back_url = "CALLBACK_URL"
        transaction_desc = "Test payment"
        response = client.stk_push(
            phone_number=phone_number,
            amount=amount,
            reference_code=reference_code,
            call_back_url=call_back_url,
            transaction_desc=transaction_desc
        )
        return HttpResponse(response)


class StkPushCallBackView(View):
    def post(self, request):
        data = request.body
        print(data)
        return HttpResponse("Success")