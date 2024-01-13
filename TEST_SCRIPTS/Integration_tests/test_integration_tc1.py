from SOURCE.Constants.apiconstants import*
from SOURCE.Helpers.api_wrapper import post_request
from SOURCE.Helpers.payload_manager import payload_create_booking
from SOURCE.Helpers.utils import common_header
from SOURCE.Helpers.common_verification import *
class Integration():

    def test_create_update_delete_booking(self):
        response = post_request(url=url_create_booking(), headers=common_header(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        print(response.json())
        print(response.status_code)

        response=patch_request(url=url_update_delete_booking(),headers=common_header(),auth=None,payload=)


