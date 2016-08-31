# -*- coding: utf-8 -*-
class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['NAME'] != '':
            return 'INFORM_NAME'
        elif attribute['PRIVATE_COMMENT_FROM_TUTOR'] != '':
            return 'INFORM_PRIVATE_COMMENT_FROM_TUTOR'
        elif attribute['LECTURE'] != '':
            return 'INFORM_LECTURE'
        else:
            return 'OTHER'
