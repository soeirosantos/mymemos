# -*- coding: utf-8 -*-

from infra.settings import Configuration

from web.application import Application

import tornado.httpserver
import tornado.ioloop
from tornado.options import options

def main():

    Configuration().configure()

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port, address=options.ip)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()