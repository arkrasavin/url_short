import json
import os

from utils.storage import check_suffix, writing_to_file
from utils.url_request import response_code, take_address
from regex_rules import creating_nickname, nickname_separation, creating_suffix, home_address


def main():
    short_path_file = os.path.join(os.path.abspath('utils/short.json'))
    nickname_path_file = os.path.join(os.path.abspath('utils/nickname.json'))
    while True:
        print('\nПрограмма для сокращения интернет-адресов\n')
        user_input = int(input('Введите:'
                               '\n1 - регистрация короткого интернет-адреса по стандартному URL'
                               '\n2 - получение и проверка домашней страницы интернет-адреса по псевдониму'
                               '\n3 - получение и проверка стандартного интернет-адреса по короткому URL'
                               '\n4 - вывод информации о всех сокращённых URL'
                               '\n5 - завершение программы\n'))

        if user_input == 1:
            user_url = input('Введите стандартный интернет-адрес для регистрации:\n').lower()
            home_url = home_address(user_url)
            nickname_url = creating_nickname(user_url)
            print(f'Псевдоним домашней страницы: {nickname_url}')
            separation_nickname_url = nickname_separation(nickname_url)
            short_url = creating_suffix(separation_nickname_url)

            if os.path.exists(short_path_file) and check_suffix(separation_nickname_url, short_url, short_path_file):
                short_url = creating_suffix(separation_nickname_url, True)

            current_dict = {
                nickname_url: home_url,
                short_url: user_url
            }

            try:
                with (open('utils/short.json', 'r') as file_1,
                      open('utils/nickname.json', 'r') as file_2):
                    file1_short = json.load(file_1)
                    file2_nickname = json.load(file_2)

                if ((nickname_url, short_url) not in (file1_short.keys(), file2_nickname)
                        and current_dict[short_url] not in file1_short.values()):
                    file1_short[short_url] = user_url
                    file2_nickname[nickname_url] = home_url
                    print('Короткий интернет-адрес: {}\n'
                          'Стандартный интернет-адрес: {}'
                          .format(short_url, user_url))

                    writing_to_file(short_path_file, file1_short)
                    writing_to_file(nickname_path_file, file2_nickname)

                else:
                    print('Короткий адрес со ссылкой уже существует')

            except FileNotFoundError:
                print('Созданы файлы:\nnickname.json\nshort.json')
                print('Короткий интернет-адрес: {}\n'
                      'Стандартный интернет-адрес: {}'.
                      format(short_url, user_url))

                current_dict = {nickname_url: home_url}
                writing_to_file(nickname_path_file, current_dict)
                current_dict = {short_url: user_url}
                writing_to_file(short_path_file, current_dict)

        elif user_input == 2:
            user_input_nickname = input('Введите псевдоним домашней страницы: ')

            try:
                print('Адрес домашней страницы:', take_address(nickname_path_file, user_input_nickname))
                print('Код ответа:', response_code(nickname_path_file, user_input_nickname))

            except FileNotFoundError as exc:
                print(f'Файл не найден, ошибка: \n{exc}')

        elif user_input == 3:
            input_short_url = input('Введите сокращенный url: ')

            try:
                print('Стандартный интернет-адрес:', take_address(short_path_file, input_short_url))
                print('Код ответа:', response_code(short_path_file, input_short_url))

            except FileNotFoundError as exc:
                print(f'Файл не найден, ошибка: \n{exc}')

        elif user_input == 4:
            with (open('utils/short.json', 'r') as file_1,
                  open('utils/nickname.json', 'r') as file_2):
                file_short, file_nick = json.load(file_1), json.load(file_2)

            print(f'Псевдонимы:\n{file_nick}\nКороткие интернет-адреса:\n{file_short}')

        elif user_input == 5:
            print('Программа завершена')
            break
