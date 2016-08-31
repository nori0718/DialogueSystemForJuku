# -*- coding: utf-8 -*-
import re


#from dialogue_system.knowledge.reader import read_names, read__private_comments, read_lectures
from dialogue_system.knowledge.reader import read_names, read_private_comment_from_tutor, read_class_comment_from_teacher


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__names = read_names()

    def extract(self, text):
        name = self.__extract_name(text)
        attribute = {
                'NAME': name, 
                'PRIVATE_COMMENT_FROM_TUTOR': read_private_comment_from_tutor(name),
                'CLASS_COMMENT_FROM_TEACHER': read_class_comment_from_teacher(name),
                }

        return attribute

    def __extract_name(self, text):
        names = [name for name in self.__names if name in text]
        names.sort(key=len, reverse=True)
        name = names[0] if len(names) > 0 else ''
        return name

