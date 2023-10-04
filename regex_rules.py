import re
import random


def check_protocol(link):
    """
    Добавляет протокол https:// в случае его отсутствия
    :param: link(str)
    :return: str
    """
    re_pattern = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)
    if re.match(re_pattern, link) is None:
        result = re.sub(r'^', 'https://', link)

        return result


def creating_nickname(link):
    """
    Создает псевдоним страницы
    :param: link(str)
    :return: str
    """
    nickname_pattern = re.sub(r'(?:http|ftp)s?://w{0,3}(\.)?', '', link)
    nickname_pattern = re.findall(r'\b\S\w+', nickname_pattern)

    return nickname_pattern[0]


def home_address(link):
    """
    Формирует домашний адрес из введенной ссылки
    :param: link(str)
    :return: str
    """
    home_url = re.sub(r'(?:http|ftp)s?://', '', link)
    home_url = re.sub(r'(/).+', '', home_url)

    return check_protocol(home_url)


def nickname_separation(nickname_string):
    """
    Сокращает псевдоним разделяя его точкой
    :param: nickname_string(str)
    :return: str
    """
    separation_line = re.sub(r'(\w{1,3})(\w{1,2})\w+', r'\1.\2', nickname_string, 1)

    return separation_line


def creating_suffix(short_nickname, flag=False):
    """
    Добавляет случайные буквы в конец, если суффикс не уникальный, то его длина += 1
    :param: short_nickname(str)
    :return: str
    """
    len_suffix = 2

    if flag:
        len_suffix += 1

    short_nickname = re.sub(r'$', '/', short_nickname)
    for _ in range(len_suffix):
        random_char = chr(random.randrange(97, 123))
        short_nickname = re.sub(r'$', random_char, short_nickname)

    return short_nickname
