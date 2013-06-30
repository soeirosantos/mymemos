# -*- coding: utf-8 -*-

import os


class Configuration(object):

    def _get_dev_settings(self):
        return dict(
                server_port = 8888,
                server_ip   = "127.0.0.1",
                db_name     = "mymemos",
                db_port     = 27017,
                db_host     = "127.0.0.1",
                db_user     = "",
                db_passwd   = "",
                debug = True,
            )

    def _get_prd_settings(self):
        #TODO: fix env variables for mongo in openshift
        return dict(
                server_port = 15001, #=> defined by command line in production 
                server_ip   = os.environ['OPENSHIFT_INTERNAL_IP'],
                db_name     = "mymemos",
                db_port     = os.environ['OPENSHIFT_'],
                db_host     = os.environ['OPENSHIFT_'],
                db_user     = os.environ['OPENSHIFT_'],
                db_passwd   = os.environ['OPENSHIFT_'],
                debug       = False,
            )
    def _set_app_path(self):
        import sys
        app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        sys.path.insert(0, app_path)

    def _set_virtutalenv(self):
        virtenv = os.environ['OPENSHIFT_HOMEDIR'] + 'app-root/runtime/python/env/tornado/'
        os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
        virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
        execfile(virtualenv, dict(__file__=virtualenv))

    def configure(self):
        self._set_app_path()

        try:
            settings = self._get_prd_settings()
            self._set_virtutalenv()
        except KeyError:
            settings = self._get_dev_settings()
            
        web_settings = dict(
            template_path= os.path.join(os.path.dirname(os.path.abspath(__file__)), "../web/templates"),
            static_path= os.path.join(os.path.dirname(os.path.abspath(__file__)), "../web/static"),
            debug=settings['debug'],
        )

        from tornado.options import define
        define("web_settings", default=web_settings, help="web settings expected by tornado.web.Application", type=dict)
        define("port", default=settings['server_port'], help="run on the given port", type=int)
        define("ip", default=settings['server_ip'], help="run on the given ip")
        define("db_host", default=settings['db_host'], help="database host")
        define("db_port", default=settings['db_port'], help="database port", type=int)
        define("db_name", default=settings['db_name'], help="database name")
        define("db_user", default=settings['db_user'], help="database user")
        define("db_passwd", default=settings['db_passwd'], help="database password")