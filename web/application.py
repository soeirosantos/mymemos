# -*- coding: utf-8 -*-

"""
Runner: Configures and starts the Tornado HTTP Server
"""

import tornado.web
from tornado.options import options
import asyncmongo

from handlers import IndexHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **options.web_settings)

        self.db = asyncmongo.Client(pool_id='mydb'
        	                       ,host=options.db_host
        	                       ,port=options.db_port
        	                       ,maxcached=10
        	                       ,maxconnections=50
        	                       ,dbname=options.db_name)