# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class CustomerId(ApiHandler):

    def get(self, id):
        print(self.args)

        return {'engagedParty': {}}, 200, None

    def delete(self, id):

        return None, 204, None

    def patch(self, id):
        print(self.json)

        return {'engagedParty': {}}, 200, None