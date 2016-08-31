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
        elif sys_act_type == 'RETURN_NAME_AND_COMMENT':
            if dialogue_act['PRIVATE_COMMENT_FROM_TUTOR']!= '':
                sent += 'チューターからコメントが届いています。{0}'.format(dialogue_act['PRIVATE_COMMENT_FROM_TUTOR'])
            if len(dialogue_act['CLASS_COMMENT_FROM_TEACHER'])!=0:
                sent += '授業についてコメントがありました。お伝えしますね。'
                for t in dialogue_act['CLASS_COMMENT_FROM_TEACHER']:
                    sent += '%s先生より。%s'%t
            sent += 'コメントは終わりです。今日は体調はどうですか？'
            
        
        # CHAT
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        else:
            print('Error')
            sys.exit(-1)

        return sent
