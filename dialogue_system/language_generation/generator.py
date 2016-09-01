# -*- coding: utf-8 -*-
import sys


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
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


        sys_act_type = dialogue_act['sys_act_type']
        if sys_act_type == 'REQUEST_SUBJECT':
            sent += '質問の科目は何ですか？'
        elif sys_act_type == 'REQUEST_TEACHER':
            sent += '質問したい先生がいたら教えてください。'
        elif sys_act_type == 'REQUEST_REPLY':
            sent += '質問内容を専用の養子にまとめてくれた？'
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        elif sys_act_type == 'INFORM_RESTAURANT':
            restaurant = dialogue_act['restaurant']
            if restaurant:
                name, address, access = restaurant['name'], restaurant['address'], restaurant['access']
                lat, lng = restaurant['lat'], restaurant['lng']
                sent += 'では、{0}がおすすめです。\n場所は{1}で{2}です。\n'.format(name, address, access)
                url = 'https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&size=640x480&zoom=14&markers={0},{1}'
                sent += url.format(lat, lng)
            else:
                sent += '申し訳ありません。条件に一致するお店が見つかりませんでした。'
        else:
            print('Error')
            sys.exit(-1)

        return sent