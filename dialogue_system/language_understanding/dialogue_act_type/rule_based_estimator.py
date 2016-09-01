# -*- coding: utf-8 -*-


class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['TEACHER'] != '':
            return 'INFORM_TEACHER'
        elif attribute['SUBJECT'] != '':
            return 'INFORM_SUBJECT'
        elif attribute['REPLY'] != '':
            return 'INFORM_REPLY'
        else:
            return 'OTHER'