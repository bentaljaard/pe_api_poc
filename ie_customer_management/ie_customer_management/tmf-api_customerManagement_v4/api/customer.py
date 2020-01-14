# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Customer(ApiHandler):

    def get(self):
        print(self.args)

        # return [], 200, {}
        return [{'id': 'customer1234', 'name': 'IE Customer 1', 'status': 'approved', 'engagedParty': {'id':'party1234', 'name': 'IE Customer Party', '@referredType':'type'}}], 200, {}


    def post(self):
        print(self.json)

        return {'engagedParty': {}}, 201, None