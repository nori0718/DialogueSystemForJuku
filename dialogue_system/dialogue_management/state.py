# -*- coding: utf-8 -*-

class DialogueState(object):

    def __init__(self):
        self.__state = {
                'NAME'                       : '',
                'PRIVATE_COMMENT_FROM_TUTOR' : '',
                'CLASS_COMMENT_FROM_TEACHER' : '',
                'CONDITION'                  : '',
                'IS_ASKED_CONDITION'         : False,
                }

    def keys(self):
        return self.__state.keys()

    def update(self, dialogue_act):
        for key, value in self.__state.items():
            self.__state[key] = dialogue_act.get(key, self.__state[key])
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

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)
