# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.customer import Customer
from .api.customer_id import CustomerId
from .api.hub import Hub
from .api.hub_id import HubId
from .api.listener_customerCreateEvent import ListenerCustomercreateevent
from .api.listener_customerAttributeValueChangeEvent import ListenerCustomerattributevaluechangeevent
from .api.listener_customerStateChangeEvent import ListenerCustomerstatechangeevent
from .api.listener_customerDeleteEvent import ListenerCustomerdeleteevent


url_prefix = 'tmf-api_customerManagement_v4'

routes = [
    dict(resource=Customer, urls=[r"/customer"], endpoint='customer'),
    dict(resource=CustomerId, urls=[r"/customer/(?P<id>[^/]+?)"], endpoint='customer_id'),
    dict(resource=Hub, urls=[r"/hub"], endpoint='hub'),
    dict(resource=HubId, urls=[r"/hub/(?P<id>[^/]+?)"], endpoint='hub_id'),
    dict(resource=ListenerCustomercreateevent, urls=[r"/listener/customerCreateEvent"], endpoint='listener_customerCreateEvent'),
    dict(resource=ListenerCustomerattributevaluechangeevent, urls=[r"/listener/customerAttributeValueChangeEvent"], endpoint='listener_customerAttributeValueChangeEvent'),
    dict(resource=ListenerCustomerstatechangeevent, urls=[r"/listener/customerStateChangeEvent"], endpoint='listener_customerStateChangeEvent'),
    dict(resource=ListenerCustomerdeleteevent, urls=[r"/listener/customerDeleteEvent"], endpoint='listener_customerDeleteEvent'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass