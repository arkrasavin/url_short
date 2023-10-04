import json
import re


def check_suffix(separation_nickname_url, short_url, path):
    """
    Проверка уникальности создаваемого суффикса в существующем json файле с короткими url адресами
    :param separation_nickname_url: разделенный точкой псевдоним
    :param short_url: короткий url
    :param path: путь к json файлу с короткими url адресами
    :return: bool
    """
    with (open(path, 'r', encoding='utf-8') as file):
        read_file = json.load(file)
    for i_key in read_file.keys():
        if (separation_nickname_url in re.findall(r'\S+(?=/)', i_key) and
                re.findall(r'(?=/)\S+', i_key) == re.findall(r'(?=/)\S+', short_url)):
            return True


def writing_to_file(path, data):
    """
    Функция записи данных в json файл
    :param path: путь к файлу
    :param data: данные для записи
    """
    with open(path, 'w+', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
