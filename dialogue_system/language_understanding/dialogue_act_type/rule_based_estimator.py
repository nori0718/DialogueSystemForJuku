# -*- coding: utf-8 -*-
class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['NAME'] != '':
            return 'NAME'
        else:
            return 'OTHER'
