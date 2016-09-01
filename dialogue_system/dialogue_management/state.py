# -*- coding: utf-8 -*-

class DialogueState(object):

    def __init__(self):
        self.__state = {
                'NAME'                       : '',
                'PRIVATE_COMMENT_FROM_TUTOR' : '',
                'CLASS_COMMENT_FROM_TEACHER' : '',
                'CONDITION'                  : '',
                'IS_ASKED_CONDITION'         : False,
                'TEACHER': None, 'SUBJECT': None, 'REPLY': None, 'PICTURE': None
                }

    def keys(self):
        return self.__state.keys()

    def update(self, dialogue_act):
        for key, value in self.__state.items():
            self.__state[key] = dialogue_act.get(key, self.__state[key])

        self.__state['TEACHER'] = dialogue_act.get('TEACHER', self.__state['TEACHER'])
        self.__state['SUBJECT'] = dialogue_act.get('SUBJECT', self.__state['SUBJECT'])
        self.__state['REPLY'] = dialogue_act.get('REPLY', self.__state['REPLY'])
        self.__state['PICTURE'] = dialogue_act.get('PICTURE', self.__state['PICTURE'])

        return


    def has(self, name):
        return self.__state.get(name, None) != None

    def get_name(self):
        return self.__state['NAME']

    def get_private_comment_from_tutor(self):
        return self.__state['PRIVATE_COMMENT_FROM_TUTOR']

    def get_class_comment_from_teacher(self):
        return self.__state['CLASS_COMMENT_FROM_TEACHER']

    def get_is_asked_condition(self):
        return self.__state['IS_ASKED_CONDITION']


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
