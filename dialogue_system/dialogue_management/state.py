# -*- coding: utf-8 -*-


class DialogueState(object):

    def __init__(self):
        self.__state = {'TEACHER': None, 'SUBJECT': None, 'REPLY': None}

    def update(self, dialogue_act):
        self.__state['TEACHER'] = dialogue_act.get('TEACHER', self.__state['TEACHER'])
        self.__state['SUBJECT'] = dialogue_act.get('SUBJECT', self.__state['SUBJECT'])
        self.__state['REPLY'] = dialogue_act.get('REPLY', self.__state['REPLY'])

    def has(self, name):
        return self.__state.get(name, None) != None

    def get_area(self):
        return self.__state['SUBJECT']

    def get_food(self):
        return self.__state['TEACHER']

    def get_budget(self):
        return self.__state['REPLY']

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)