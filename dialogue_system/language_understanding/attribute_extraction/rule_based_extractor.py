# -*- coding: utf-8 -*-
import re


from dialogue_system.knowledge.reader import read_genres, read_locations, read_subject, read_teacher, read_yes, read_no
from dialogue_system.language_understanding.utils.utils import kansuji2arabic


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__locations = read_locations()
        self.__genres = read_genres()
        self.__subject = read_subject()
        self.__teacher = read_teacher()
        self.__yes = read_yes()
        self.__no = read_no()


    def extract(self, text):
        attribute = {'SUBJECT': self.__extract_subject(text), 'TEACHER': self.__extract_teacher(text),
                     'REPLY': self.__extract_reply(text)}

        return attribute

    def __extract_subject(self, text): #質問教科
        subjects = [loc for loc in self.__subject if loc in text]
        subjects.sort(key=len, reverse=True)
        subject = subjects[0] if len(subjects) > 0 else ''

        return subject

    def __extract_reply(self, text): #返答診断
        replys = [loc for loc in self.__yes if loc in text]
        replys.sort(key=len, reverse=True)
        reply = "yes" if len(replys) > 0 else ''
        if reply in "":
            replys = [loc for loc in self.__no if loc in text]
            replys.sort(key=len, reverse=True)
            reply = "no" if len(replys) > 0 else ''

        return reply


    def __extract_teacher(self, text): #先生の判別
        for teacher_full, teachers in self.__teacher.items():
            for teacher in teachers:
                if teacher in text:
                    return teacher_full
        return ''

    def __extract_genre(self, text):
        for food_genre, foods in self.__genres.items():
            for food in foods:
                if food in text:
                    return food_genre
        return ''

    def __extract_budget(self, text):
        pattern = r'\d+円|[一二三四五六七八九十壱弐参拾百千万萬億兆〇]+円'
        match_obj = re.findall(pattern, text)
        budget_str = match_obj[0][:-1] if len(match_obj) > 0 else ''
        budget_int = kansuji2arabic(budget_str)

        return budget_int