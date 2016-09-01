# -*- coding: utf-8 -*-
import sys

class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
        sys_act_type = dialogue_act['sys_act_type']


        if 'SUBJECT' in dialogue_act:
            sent += '質問の科目は{0}ですね。'.format(dialogue_act['SUBJECT'])
        if 'TEACHER' in dialogue_act:
            sent += '{0}先生ですね。'.format(dialogue_act['TEACHER'])
        if 'REPLY' in dialogue_act:
            judge = '{0}'.format(dialogue_act['REPLY'])
            if judge in "yes":
                sent += "ありがとう！記憶するから僕に見せてくれるかな？"
            elif judge in "no":
                sent += "まとめてからまた持って来てね"
            else:
                sent += "質問内容がよくわからないな"
        if 'PICTURE' in dialogue_act:
            sent += '記憶したよ'


        # Confirmation
        if 'NAME' in dialogue_act:
            sent += '{0}さんですね？おはようございます。'.format(dialogue_act['NAME'])
        elif 'CONDITION' in dialogue_act:
            if dialogue_act['CONDITION']=='LOW':
                sent += '無理をしないでね。体調が悪くなったらすぐに職員に相談してね。' 
            elif dialogue_act['CONDITION']=='NEUTRAL':
                sent += '今日も頑張ろう。'
            elif dialogue_act['CONDITION']=='HIGH':
                sent += '絶好調だね。バリバリ勉強していこう。'
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
            
        elif sys_act_type == 'IS_QUESTION':
            sent += '最近何か質問とかはある？'



        if sys_act_type == 'REQUEST_SUBJECT':
            sent += '質問の科目は何ですか？'
        elif sys_act_type == 'REQUEST_TEACHER':
            sent += '質問したい先生がいたら教えてください。'
        elif sys_act_type == 'REQUEST_REPLY':
            sent += '質問内容を専用の用紙にまとめてくれた？'
        elif sys_act_type == 'REQUEST_PICTURE':
            sent += '記憶したいから見せてくれるかな？準備が整ったら頑張ってって言ってね'


        # CHAT
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        else:
            print('Error')
            sys.exit(-1)

        return sent
