# -*- coding: utf-8 -*-
import sys

class LanguageGenerator(object):

    def __init__(self):
        pass

    def __confirmation(self, dialogue_act):
        sent = ''
        # Confirmation
        if 'NAME' in dialogue_act:
            sent += '{0}さんですね？おはようございます。'.format(dialogue_act['NAME'])
        elif 'CONDITION' in dialogue_act:
            if dialogue_act['CONDITION']=='LOW':
                sent += '無理をしないでね。体調が悪くなったらすぐに職員に相談してね。' 
            elif dialogue_act['CONDITION']=='NEUTRAL':
                sent += 'いつも頑張っているね。今日も頑張ろう。'
            elif dialogue_act['CONDITION']=='HIGH':
                sent += '絶好調だね。バリバリ勉強していこう。'
        return sent

    def __request(self, sys_act_type):
        sent = ''
        # REQUEST
        if sys_act_type == 'REQUEST_NAME':
            sent += '名前を教えてください！'       
        return sent

    def __inform(self, sys_act_type):
        # INFORM
        if sys_act_type == 'RETURN_NAME_AND_COMMENT':
            if dialogue_act['PRIVATE_COMMENT_FROM_TUTOR']!= '':
                sent += 'チューターからコメントが届いています。{0}'.format(dialogue_act['PRIVATE_COMMENT_FROM_TUTOR'])
            if len(dialogue_act['CLASS_COMMENT_FROM_TEACHER'])!=0:
                sent += '授業についてコメントがありました。お伝えしますね。'
                for t in dialogue_act['CLASS_COMMENT_FROM_TEACHER']:
                    sent += '%s先生より。%s'%t
            sent += 'コメントは終わりです。今日は体調はどうですか？'

        elif sys_act_type == 'IS_QUESTION':
            sent += '最近何か質問とかはある？あったら科目を教えてね。'
        
        # CHAT
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        else:
            print('Error')
            sys.exit(-1)

    def generate_sentence(self, dialogue_act):
        sent = ''
        sys_act_type = dialogue_act['sys_act_type']

        sent += __confirmation(dialogue_act)
        sent += __request(sys_act_type)
        sent += __inform(sys_act_type)
        sent += __inform(sys_act_type)

        return sent
