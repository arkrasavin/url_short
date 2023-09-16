import json
import requests


#
def response_code(path, request_key):
    with open(path, 'r', encoding='utf-8') as file_read:
        file = json.load(file_read)

    address = file.get(request_key)

    if address:
        response_status = requests.get(address).status_code

        return response_status


def take_address(path, request_key):
    with open(path, 'r', encoding='utf-8') as read_file:
        file_decoder = json.load(read_file)
    response_address = file_decoder.get(request_key, 'Адрес не найден')

    return response_address
