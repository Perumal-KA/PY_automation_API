def payload_create_booking():
    payload={
    "firstname" : "Perumal",
    "lastname" : "K A",
    "totalprice" : 145,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-08-01"
    },
    "additionalneeds" : "Breakfast"}
    return payload

