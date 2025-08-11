import os
import json
from pathlib import Path
from hashlib import md5


working_directory = Path.cwd()


# try loading saved hashes
try:
    index = json.load(open('file_index.json', 'r'))
except FileNotFoundError:
    print('File index not found, creating a new one...')
    index = {}


def check_hash(filepath):
    filehash = md5(filepath.open('rb').read()).hexdigest()
    if filepath.name in index and index[filepath.name] == filehash:
        return True
    index[filepath.name] = filehash
    return False


# compile resources
for filepath in working_directory.rglob('*.qrc'):
    filepath = filepath.resolve()
    if check_hash(filepath):
        continue
    print(f'Compiling {filepath.name}...')
    new_name = f'{filepath.with_suffix("").name}_rc.py'
    new_path = working_directory.joinpath(new_name).resolve()
    os.system(f'pyside6-rcc {filepath} -o {new_path}')


# compile widget UIs
for filepath in working_directory.rglob('*.ui'):
    filepath = filepath.resolve()
    if check_hash(filepath):
        continue
    print(f'Compiling {filepath.name}...')
    new_name = f'ui_{filepath.name}'
    new_path = filepath.with_name(new_name).with_suffix('.py')
    os.system(f'pyside6-uic {filepath} -o {new_path}')


# save hashes
json.dump(index, open("file_index.json", "w"), indent=2, sort_keys=True)
