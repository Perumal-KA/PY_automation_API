import pytest
import requests
import allure
import json

from SOURCE.Constants.apiconstants import url_create_booking,url_create_token,url_update_booking,url_delete_booking,url_get_booking
from SOURCE.Helpers.api_wrapper import post_request,patch_request,delete_request,get_request
from SOURCE.Helpers.payload_manager import payload_create_booking,payload_updateAllData_booking
from SOURCE.Helpers.utils import common_auth,common_header,headers_withToken
from SOURCE.Helpers.common_verification import verify_key,verify_http_code,verify_token,verify_status_message

booking_id=None
token=None

class Test_Integration(object):

    def test_create_new_token(self):
        global token
        response=post_request(url_create_token(),headers=common_header(),auth=None,payload=common_auth(),in_json=False)
        verify_http_code(response,200)
        print(response.text)
        token = response.json()["token"]
        verify_token(token)



    def test_create_post_booking(self):
        global booking_id
        response=post_request(url=url_create_booking(),headers=common_header(),auth=None,payload=payload_create_booking(),in_json=False)
        verify_http_code(response,200)
        print(response.json())
        booking_id=response.json()["bookingid"]
        verify_key(booking_id)
        return booking_id

    def test_update_booking(self):
        response=patch_request(url_update_booking(booking_id),headers=headers_withToken(token),auth=None,payload=payload_updateAllData_booking(),in_json=False)
        verify_http_code(response,200)
        print(response.json())






    def test_delete_booking(self):
        response=delete_request(url=url_delete_booking(booking_id),headers=headers_withToken(token),auth=None,in_json=False)
        verify_http_code(response,201)
        print(response.status_code)

    def test_get_updated_booking(self):
        response=get_request(url_get_booking(booking_id),auth=None,in_json=False)
        verify_http_code(response,404)
        print(response.status_code)
        print(response.text)







