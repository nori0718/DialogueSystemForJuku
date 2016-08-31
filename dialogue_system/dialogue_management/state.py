# -*- coding: utf-8 -*-

class DialogueState(object):

    def __init__(self):
        self.__state = {
                'NAME'                       : None,
                'PRIVATE_COMMENT_FROM_TUTOR' : None,
                'LECTURE'                    : None,
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

    def get_lecture(self):
        return self.__state['LECTURE']

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)
