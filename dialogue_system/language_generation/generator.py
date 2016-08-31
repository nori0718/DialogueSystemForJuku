# -*- coding: utf-8 -*-
import sys

class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
        sys_act_type = dialogue_act['sys_act_type']

        # Confirmation
        if 'NAME' in dialogue_act:
            sent += '{0}さんですね？おはようございます。'.format(dialogue_act['NAME'])

        # REQUEST
        if sys_act_type == 'REQUEST_NAME':
            sent += '名前を教えてください！'

        # INFORM
        elif sys_act_type == 'INFORM_PRIVATE_COMMENT_FROM_TUTOR':
            sent += 'チューターからコメントが届いています。%s'
        elif sys_act_type == 'INFORM_PRIVATE_COMMENT_FROM_TUTOR':
            sent += 'コメントはありませんでした。'

        # CHAT
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        else:
            print('Error')
            sys.exit(-1)

        return sent
