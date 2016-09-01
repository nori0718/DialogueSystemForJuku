# -*- coding: utf-8 -*-
import os


API_TOKEN = os.environ.get('SLACK_API_KEY', '')
 
default_reply = "すいません。その言葉わかりません"

PLUGINS = [
    'plugins',
]
