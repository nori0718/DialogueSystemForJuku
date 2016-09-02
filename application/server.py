# -*- coding: utf-8 -*-
import sys, os

import tornado.ioloop
import tornado.web
import tornado.websocket

from dialogue_system.bot import Bot


class MessageServer(tornado.websocket.WebSocketHandler):
    bots = {}

    def check_origin(self, origin):
        return True

    def open(self):
        print('on open')
        self.bots[self] = Bot()
        self.write_message('こんにちは！')

    def on_message(self, message):
        print('on message')
        print(message)
        bot = self.bots[self]
        self.write_message(bot.reply(message))

    def on_close(self):
        print('on close')
        del self.bots[self]

class ManagementHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
            (r'/ws', MessageServer),
            (r'/', ManagementHandler),
        ],
        template_path=os.path.join(os.getcwd(),  "templates"),
        static_path=os.path.join(os.getcwd(),  "static"),
        )

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()
