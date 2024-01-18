#helps you to read json files and provide you json data

import json

def get_payload_auth():
    #raed from auth.json and return
    file_data=open("SOURCE/Constants/auth.json")
    data=json.loads(file_data)  #json.loads---> parse a valid json string to python dictionary
    file_data.close()
    return data

def common_header():
    headers={"Content-Type": "application/json"}
    return headers

def common_auth():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def headers_withToken(test_create_token):
    temp_token = "token=" + test_create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers