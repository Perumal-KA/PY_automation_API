#add your constants
#add url constants, Python--> functions

def base_url():
    #change based on the env.json--> stage, pre-prod, prod
    #in future base-url can be changed on the env
    return "https://restful-booker.herokuapp.com"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"

def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+booking_id

