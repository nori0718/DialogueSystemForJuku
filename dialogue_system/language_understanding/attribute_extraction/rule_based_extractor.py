# -*- coding: utf-8 -*-
import re


#from dialogue_system.knowledge.reader import read_names, read__private_comments, read_lectures
from dialogue_system.knowledge.reader import read_names


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__names = read_names()

    def extract(self, text):
        attribute = {
                'NAME': self.__extract_name(text), 
                'PRIVATE_COMMENT_FROM_TUTOR': self.__extract_private_comment_from_tutor(text),
                'LECTURE': self.__extract_lecture(text)
                }

        return attribute

    def __extract_name(self, text):
        names = [name for name in self.__names if name in text]
        names.sort(key=len, reverse=True)
        name = names[0] if len(names) > 0 else ''
        return name

    def __extract_private_comment_from_tutor(self, text):
        #if self.get_name() == '':
        #    return ''
        #private_comments = read_private_comments(self.__state['name'])
        #private_comments = [i if i.endswith('。') else i+'。'  for i in private_comments]
        #return ''.join(private_comments)
        return

    def __extract_lecture(self, text):
        #if self.get_name() == '':
        #    return ''
        #lectures = read_lectures(self.__state['name'],day)
        #return lectures
        return 
