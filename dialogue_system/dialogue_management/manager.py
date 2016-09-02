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
        if self.update_dialogue_state
        
        if not self.dialogue_state.has('NAME'):
            sys_act['sys_act_type'] = 'REQUEST_NAME'
        elif dialogue_act['user_act_type'] == 'NAME':
            sys_act['sys_act_type'] = 'RETURN_NAME_AND_COMMENT'
        elif dialogue_act['user_act_type'] == 'CONDITION':
            sys_act['sys_act_type'] = 'IS_QUESTION'
        elif dialogue_act['user_act_type'] == 'OTHER':
            api = DocomoDialogAPI()
            reply = api.reply(dialogue_act['utt'])
            sys_act['sys_act_type'] = 'CHAT'
            sys_act['utt'] = reply
        else:
            self.dialogue_state.clear()

        return sys_act
