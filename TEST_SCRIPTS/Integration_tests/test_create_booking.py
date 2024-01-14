"""
Author: Perumal
obj: create and verify POST requests
TC1: verify status code, headers
TC2: verify body--> booking_id
TC3: verify json is valid
"""


import pytest
import requests

from SOURCE.Constants.apiconstants import url_create_booking
from SOURCE.Helpers.api_wrapper import post_request
from SOURCE.Helpers.payload_manager import payload_create_booking
from SOURCE.Helpers.utils import common_header
from SOURCE.Helpers.common_verification import*


class Testintegration(object):
    def test_create_booking_tc1(self):
        # call the fn to make request
        # we will not see how we are making request in TC
        response = post_request(url=url_create_booking(), headers=common_header(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response,200)
        booking_id=response.json()['bookingid']
        verify_key(booking_id)

        print(response.status_code)
        print(response.json())

    # assert True == True   # assertion (expected result = actual result)


'''def test_create_booking_tc2(self):

          assert True == False


    def test_create_booking_tc3(self):
           assert True == True'''
