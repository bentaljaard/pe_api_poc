# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Hub(ApiHandler):

    def post(self):
        print(self.json)

        return {'id': 'something', 'callback': 'something'}, 201, None