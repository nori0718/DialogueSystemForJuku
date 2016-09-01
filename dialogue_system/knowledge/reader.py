# -*- coding: utf-8 -*-
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_locations():
    file_path = os.path.join(BASE_DIR, 'locations.txt')
    with open(file_path, 'rb') as f:
        locations = [loc.decode('utf-8').strip() for loc in f]

    return locations


def read_genres():
    file_path = os.path.join(BASE_DIR, 'genre.yaml')
    with open(file_path, 'rb') as f:
        genres = yaml.load(f)

    return genres

def read_subject():
    file_path = os.path.join(BASE_DIR, 'subject.txt')
    with open(file_path, 'rb') as f:
        subjects = [loc.decode('utf-8').strip() for loc in f]

    return subjects

def read_teacher():
    file_path = os.path.join(BASE_DIR, 'teacher.yaml')
    with open(file_path, 'rb') as f:
        teachers = yaml.load(f)

    return teachers

def read_yes():
    file_path = os.path.join(BASE_DIR, 'yes.txt')
    with open(file_path, 'rb') as f:
        okreply = [loc.decode('utf-8').strip() for loc in f]

    return okreply

def read_no():
    file_path = os.path.join(BASE_DIR, 'no.txt')
    with open(file_path, 'rb') as f:
        noreply = [loc.decode('utf-8').strip() for loc in f]

    return noreply
