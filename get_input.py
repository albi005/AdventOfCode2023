import sys
import urllib.request
from urllib.request import Request
from pathlib import Path


# Advent of Code runner

def get_number(file_name):
    assert file_name.endswith('.rs')
    assert len(file_name) == 6
    number = int(file_name[0:2])
    return number

def get_token():
    token = None
    with open('token.txt', 'r') as file:
        token = file.read()
    token = token.strip()
    return token

# download to inputs/XX.txt
def download_input(day):
    session = get_token()
    url = f'https://adventofcode.com/2023/day/{day}/input'
    file_name = f'inputs/{day:02}.txt'
    req = Request(url, headers={'Cookie':f'session={session}'})
    text = urllib.request.urlopen(req).read().decode('utf-8')
    Path('inputs').mkdir(parents=True, exist_ok=True)
    with open(file_name, 'w') as file:
        file.write(text)

day = get_number(sys.argv[1])
download_input(day)

# python is garbage
