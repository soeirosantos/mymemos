    # -*- coding: utf-8 -*-

import tornado.web
from tornado import gen
import datetime

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html", message=None)

    @tornado.web.asynchronous
    def post(self):

        memo_note = self.get_argument("memo", None)

        memo = {'note': memo_note}
        
        self.application.db.memos.insert(memo, callback=self._post_callback)


    def _post_callback(self, response, error):
        self.render("index.html", message="Memorizado!")
