import os.path
import logging
import socket
import select
import json
import os

from kn.utils.whim import WhimDaemon, WhimClient

from kn import settings

from kn.utils.giedo.db import update_db
from kn.utils.giedo.postfix import generate_postfix_map

class Giedo(WhimDaemon):
        def __init__(self):
                super(Giedo, self).__init__(settings.GIEDO_SOCKET)
                self.daan = WhimClient(settings.DAAN_SOCKET)

        def handle(self, d):
                # For now, be stupid, and always update everything
                update_db(self)
                self.daan.send({'type': 'postfix',
                                'map': generate_postfix_map(self)})