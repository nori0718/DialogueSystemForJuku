# -*- coding: utf-8 -*-
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_names():
    file_path = os.path.join(BASE_DIR, 'names.txt')
    with open(file_path, 'rb') as f:
        names = [name.decode('utf-8').strip() for name in f]
    return names

