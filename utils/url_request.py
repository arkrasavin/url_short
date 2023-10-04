import json
import requests


#
def response_code(path, request_key):
    """
    Функция возвращающая код ответа от сервера по ключу запроса
    :param path: путь к файлу
    :param request_key: ключ запроса проверки статуса сервера
    :return: int
    """
    with open(path, 'r', encoding='utf-8') as file_read:
        file = json.load(file_read)

    address = file.get(request_key)

    if address:
        response_status = requests.get(address).status_code

        return response_status


def take_address(path, request_key):
    """
    Функция возвращающая интернет адрес по ключу запроса
    :param path: путь к файлу
    :param request_key: ключ для запроса
    :return: str
    """
    with open(path, 'r', encoding='utf-8') as read_file:
        file_decoder = json.load(read_file)
    response_address = file_decoder.get(request_key, 'Адрес не найден')

    return response_address
