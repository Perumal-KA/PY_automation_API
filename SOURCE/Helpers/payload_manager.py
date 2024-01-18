import json


def payload_create_booking():
    payload={
    "firstname" : "Vijay",
    "lastname" : "K A",
    "totalprice" : 148,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-08-01"
    },
    "additionalneeds" : "Breakfast"}
    return payload

def payload_auth():
    payload=json.dumps({
    "username" : "admin",
    "password" : "password123"})
    return payload

def payload_updateAllData_booking():
    payload = {
        "firstname": "perumal",
        "lastname": "VJ",
        "totalprice": 200,
        "depositpaid": "False",
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Breakfast,Lunch"
    }
    return payload
