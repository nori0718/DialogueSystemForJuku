# -*- coding: utf-8 -*-
from copy import deepcopy

from dialogue_system.dialogue_management.state import DialogueState
from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        sys_act = deepcopy(dialogue_act)
        if dialogue_act['user_act_type'] == 'OTHER':
            api = DocomoDialogAPI()
            reply = api.reply(dialogue_act['utt'])
            sys_act['sys_act_type'] = 'CHAT'
            sys_act['utt'] = reply
        elif not self.dialogue_state.has('NAME'):
            sys_act['sys_act_type'] = 'REQUEST_NAME'
        else:
            name = self.dialogue_state.get_name()
            sys_act['sys_act_type'] = 'INFORM_PRIVATE_COMMENT_FROM_TUTOR'
            self.dialogue_state.clear()

        return sys_act
