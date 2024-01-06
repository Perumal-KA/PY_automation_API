#helps you to read json files and provide you json data

import json

def get_payload_auth():
    #raed from auth.json and return
    file_data=open("SOURCE/Constants/auth.json")
    data=json.loads(file_data)  #json.loads---> parse a valid json string to python dictionary
    file_data.close()
    return data