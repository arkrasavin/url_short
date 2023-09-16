import json
import re


def check_suffix(separation_nickname_url, short_url, path):
    with (open(path, 'r', encoding='utf-8') as file):
        read_file = json.load(file)
    for i in read_file.keys():
        if (separation_nickname_url in re.findall(r'\S+(?=/)', i) and
                re.findall(r'(?=/)\S+', i) == re.findall(r'(?=/)\S+', short_url)):
            return True
