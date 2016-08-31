# -*- coding: utf-8 -*-
from slackbot.bot import Bot
import sys

def main():
    sys.path.append('./../')
    bot = Bot()
    bot.run()
 
if __name__ == "__main__":
    main()
