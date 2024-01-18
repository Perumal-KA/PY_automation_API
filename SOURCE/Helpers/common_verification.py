#https status code
def verify_http_code(response_data,expected_data):
    assert response_data.status_code==int(expected_data), " Expected HTTP status:"+ int(expected_data)

def verify_status_message(response_data,expected_data):
    assert response_data==expected_data,"Expected status message displayed:"+ expected_data

def verify_key(key):
    assert int(key)!=0, " key is non empty"+ key
    assert int(key)>0, " key should be greater than zero:"+ key

def verify_token(token):
    assert token is not None, "Token is not empty:" + token