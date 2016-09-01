# -*- coding: utf-8 -*-
import re


#from dialogue_system.knowledge.reader import read_names, read__private_comments, read_lectures
from dialogue_system.knowledge.reader import read_names, read_private_comment_from_tutor, read_class_comment_from_teacher, read_condition, read_subject, read_teacher, read_yes, read_no, read_picture

import MeCab


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__names = read_names()
        self.__subject = read_subject()
        self.__teacher = read_teacher()
        self.__yes = read_yes()
        self.__no = read_no()
        self.__picture = read_picture()

    def extract(self, bot, text):
        name = self.__extract_name(text)
        attribute = {
                'NAME': name, 
                'PRIVATE_COMMENT_FROM_TUTOR': read_private_comment_from_tutor(name),
                'CLASS_COMMENT_FROM_TEACHER': read_class_comment_from_teacher(name),
                'CONDITION': self.__extract_condition(text, bot),
                'SUBJECT': self.__extract_subject(text),
                'TEACHER': self.__extract_teacher(text),
                'REPLY': self.__extract_reply(text),
                'PICTURE': self.__extract_picture(text)
               }


        return attribute

    def __extract_name(self, text):
        names = [name for name in self.__names if name in text]
        names.sort(key=len, reverse=True)
        name = names[0] if len(names) > 0 else ''
        return name
    
    def __extract_condition(self, text, bot):
        if bot.manager.dialogue_state.get_is_asked_condition():
            return ''
        if bot.manager.dialogue_state.get_name() != '': 
            bot.manager.dialogue_state.update({'IS_ASKED_CONDITION':True})
            return read_condition(text)
        else:
            return ''


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

    def __extract_picture(self, text): #写真
        subjects = [loc for loc in self.__picture if loc in text]
        subjects.sort(key=len, reverse=True)
        subject = subjects[0] if len(subjects) > 0 else ''

        return subject
