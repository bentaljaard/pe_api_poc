# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Customer(ApiHandler):

    def get(self):
        print(self.args)

        return [{'id': 'customer1234', 'name': 'NL Customer 1', 'status': 'approved', 'engagedParty': {'id':'party1234', 'name': 'NL Customer Party', '@referredType':'type'}}], 200, {}

    def post(self):
        print(self.json)

        return {'engagedParty': {}}, 201, None