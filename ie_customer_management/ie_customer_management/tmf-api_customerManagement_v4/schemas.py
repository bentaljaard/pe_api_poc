# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/tmf-api/customerManagement/v4/'

definitions = {'definitions': {'AccountRef': {'type': 'object', 'description': 'Account reference. A account may be a party account or a financial account.', 'required': ['name'], 'properties': {'id': {'type': 'string', 'description': 'Unique identifier of the account'}, 'href': {'type': 'string', 'description': 'Reference of the account'}, 'description': {'type': 'string', 'description': 'Detailed description of the account'}, 'name': {'type': 'string', 'description': 'Name of the account'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}, '@referredType': {'type': 'string', 'description': 'The actual type of the target instance when needed for disambiguation.'}}}, 'AgreementRef': {'type': 'object', 'description': 'Agreement reference. An agreement represents a contract or arrangement, either written or verbal and sometimes enforceable by law, such as a service level agreement or a customer price agreement. An agreement involves a number of other business entities, such as products, services, and resources and/or their specifications.', 'properties': {'id': {'type': 'string', 'description': 'Unique identifier of a related entity.'}, 'href': {'type': 'string', 'description': 'Reference of the related entity.'}, 'name': {'type': 'string', 'description': 'Name of the agreement'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}, '@referredType': {'type': 'string', 'description': 'The actual type of the target instance when needed for disambiguation.'}}, 'required': ['id']}, 'Any': {}, 'Characteristic': {'type': 'object', 'description': 'Describes a given characteristic of an object or entity through a name/value pair.', 'required': ['name', 'value'], 'properties': {'name': {'type': 'string', 'description': 'Name of the characteristic'}, 'valueType': {'type': 'string', 'description': 'Data type of the value of the characteristic'}, 'value': {'$ref': '#/definitions/Any', 'description': 'The value of the characteristic'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'ContactMedium': {'type': 'object', 'description': 'Indicates the contact medium that could be used to contact the party.', 'required': ['mediumType', 'characteristic'], 'properties': {'mediumType': {'type': 'string', 'description': 'Type of the contact medium, such as: email address, telephone number, postal address'}, 'preferred': {'type': 'boolean', 'description': 'If true, indicates that is the preferred contact medium'}, 'characteristic': {'$ref': '#/definitions/MediumCharacteristic', 'description': 'Any additional characteristic(s) of this contact medium'}, 'validFor': {'$ref': '#/definitions/TimePeriod', 'description': 'The time period that the contact medium is valid for'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'CreditProfile': {'type': 'object', 'description': 'Credit profile for the party (containing credit scoring, ...). By default only the current credit profile  is retrieved. It can be used as a list to give the party credit profiles history, the first one in the list will be the current one.', 'required': ['creditProfileDate', 'validFor'], 'properties': {'creditProfileDate': {'type': 'string', 'format': 'date-time', 'description': 'The date the profile was established'}, 'creditRiskRating': {'type': 'integer', 'description': 'This is an integer whose value is used to rate the risk'}, 'creditScore': {'type': 'integer', 'description': 'A measure of a person or organizations creditworthiness calculated on the basis of a combination of factors such as their income and credit history'}, 'validFor': {'$ref': '#/definitions/TimePeriod', 'description': 'The period for which the profile is valid'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'Customer': {'type': 'object', 'required': ['engagedParty'], 'properties': {'id': {'type': 'string', 'description': 'Unique identifier for Customers'}, 'href': {'type': 'string', 'description': 'Url used to reference the customer.'}, 'name': {'type': 'string', 'description': 'A word, term, or phrase by which the Customer is known and distinguished from other Customers.'}, 'status': {'type': 'string', 'description': 'Used to track the lifecycle status of the customer.'}, 'statusReason': {'type': 'string', 'description': 'A string providing an explanation on the value of the status lifecycle. For instance if the status is Rejected, statusReason will provide the reason for rejection.'}, 'account': {'type': 'array', 'items': {'$ref': '#/definitions/AccountRef'}}, 'agreement': {'type': 'array', 'items': {'$ref': '#/definitions/AgreementRef'}}, 'characteristic': {'type': 'array', 'items': {'$ref': '#/definitions/Characteristic'}, 'description': 'Describes the characteristic of a customer.'}, 'contactMedium': {'type': 'array', 'items': {'$ref': '#/definitions/ContactMedium'}}, 'creditProfile': {'type': 'array', 'items': {'$ref': '#/definitions/CreditProfile'}}, 'engagedParty': {'$ref': '#/definitions/RelatedParty', 'description': 'The party - an organization or an individual - that is engaged as a customer.'}, 'paymentMethod': {'type': 'array', 'items': {'$ref': '#/definitions/PaymentMethodRef'}}, 'relatedParty': {'type': 'array', 'items': {'$ref': '#/definitions/RelatedParty'}}, 'validFor': {'$ref': '#/definitions/TimePeriod', 'description': 'The time period that the Customer is valid for.'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'Customer_Create': {'type': 'object', 'description': '\nSkipped properties: id,href', 'required': ['engagedParty', 'name'], 'properties': {'name': {'type': 'string', 'description': 'A word, term, or phrase by which the Customer is known and distinguished from other Customers.'}, 'status': {'type': 'string', 'description': 'Used to track the lifecycle status of the customer.'}, 'statusReason': {'type': 'string', 'description': 'A string providing an explanation on the value of the status lifecycle. For instance if the status is Rejected, statusReason will provide the reason for rejection.'}, 'account': {'type': 'array', 'items': {'$ref': '#/definitions/AccountRef'}}, 'agreement': {'type': 'array', 'items': {'$ref': '#/definitions/AgreementRef'}}, 'characteristic': {'type': 'array', 'items': {'$ref': '#/definitions/Characteristic'}, 'description': 'Describes the characteristic of a customer.'}, 'contactMedium': {'type': 'array', 'items': {'$ref': '#/definitions/ContactMedium'}}, 'creditProfile': {'type': 'array', 'items': {'$ref': '#/definitions/CreditProfile'}}, 'engagedParty': {'$ref': '#/definitions/RelatedParty', 'description': 'The party - an organization or an individual - that is engaged as a customer.'}, 'paymentMethod': {'type': 'array', 'items': {'$ref': '#/definitions/PaymentMethodRef'}}, 'relatedParty': {'type': 'array', 'items': {'$ref': '#/definitions/RelatedParty'}}, 'validFor': {'$ref': '#/definitions/TimePeriod', 'description': 'The time period that the Customer is valid for.'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'Customer_Update': {'type': 'object', 'description': '\nSkipped properties: id,href', 'required': ['engagedParty'], 'properties': {'name': {'type': 'string', 'description': 'A word, term, or phrase by which the Customer is known and distinguished from other Customers.'}, 'status': {'type': 'string', 'description': 'Used to track the lifecycle status of the customer.'}, 'statusReason': {'type': 'string', 'description': 'A string providing an explanation on the value of the status lifecycle. For instance if the status is Rejected, statusReason will provide the reason for rejection.'}, 'account': {'type': 'array', 'items': {'$ref': '#/definitions/AccountRef'}}, 'agreement': {'type': 'array', 'items': {'$ref': '#/definitions/AgreementRef'}}, 'characteristic': {'type': 'array', 'items': {'$ref': '#/definitions/Characteristic'}, 'description': 'Describes the characteristic of a customer.'}, 'contactMedium': {'type': 'array', 'items': {'$ref': '#/definitions/ContactMedium'}}, 'creditProfile': {'type': 'array', 'items': {'$ref': '#/definitions/CreditProfile'}}, 'engagedParty': {'$ref': '#/definitions/RelatedParty', 'description': 'The party - an organization or an individual - that is engaged as a customer.'}, 'paymentMethod': {'type': 'array', 'items': {'$ref': '#/definitions/PaymentMethodRef'}}, 'relatedParty': {'type': 'array', 'items': {'$ref': '#/definitions/RelatedParty'}}, 'validFor': {'$ref': '#/definitions/TimePeriod', 'description': 'The time period that the Customer is valid for.'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'EntityRef': {'type': 'object', 'description': 'Entity reference schema to be use for all entityRef class.', 'properties': {'id': {'type': 'string', 'description': 'Unique identifier of a related entity.'}, 'href': {'type': 'string', 'description': 'Reference of the related entity.'}, 'name': {'type': 'string', 'description': 'Name of the related entity.'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}, '@referredType': {'type': 'string', 'description': 'The actual type of the target instance when needed for disambiguation.'}}, 'required': ['id']}, 'MediumCharacteristic': {'type': 'object', 'description': 'Describes the contact medium characteristics that could be used to contact a party (an individual or an organization)', 'properties': {'city': {'type': 'string', 'description': 'The city'}, 'contactType': {'type': 'string', 'description': 'The type of contact, for example: phone number such as mobile, fixed home, fixed office. postal address such as shipping instalation…'}, 'country': {'type': 'string', 'description': 'The country'}, 'emailAddress': {'type': 'string', 'description': 'Full email address in standard format'}, 'faxNumber': {'type': 'string', 'description': 'The fax number of the contact'}, 'phoneNumber': {'type': 'string', 'description': 'The primary phone number of the contact'}, 'postCode': {'type': 'string', 'description': 'Postcode'}, 'socialNetworkId': {'type': 'string', 'description': 'Identifier as a member of a social network'}, 'stateOrProvince': {'type': 'string', 'description': 'State or province'}, 'street1': {'type': 'string', 'description': 'Describes the street'}, 'street2': {'type': 'string', 'description': 'Complementary street description'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}}}, 'PaymentMethodRef': {'type': 'object', 'description': 'PaymentMethod reference. A payment method defines a specific mean of payment (e.g direct debit).', 'properties': {'id': {'type': 'string', 'description': 'Unique identifier of the payment mean'}, 'href': {'type': 'string', 'description': 'Reference of the payment mean'}, 'name': {'type': 'string', 'description': 'Name of the payment mean'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}, '@referredType': {'type': 'string', 'description': 'The actual type of the target instance when needed for disambiguation.'}}, 'required': ['id']}, 'RelatedParty': {'type': 'object', 'description': 'Related Entity reference. A related party defines party or party role linked to a specific entity.', 'required': ['@referredType', 'id'], 'properties': {'id': {'type': 'string', 'description': 'Unique identifier of a related entity.'}, 'href': {'type': 'string', 'description': 'Reference of the related entity.'}, 'name': {'type': 'string', 'description': 'Name of the related entity.'}, 'role': {'type': 'string', 'description': 'Role played by the related party'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name'}, '@referredType': {'type': 'string', 'description': 'The actual type of the target instance when needed for disambiguation.'}}}, 'TimePeriod': {'type': 'object', 'description': 'A period of time, either as a deadline (endDateTime only) a startDateTime only, or both', 'properties': {'endDateTime': {'type': 'string', 'format': 'date-time', 'description': 'End of the time period, using IETC-RFC-3339 format'}, 'startDateTime': {'type': 'string', 'format': 'date-time', 'description': 'Start of the time period, using IETC-RFC-3339 format. If you define a start, you must also define an end'}}}, 'EventSubscription': {'type': 'object', 'description': 'Sets the communication endpoint address the service instance must use to deliver notification information', 'required': ['id', 'callback'], 'properties': {'id': {'type': 'string', 'description': 'Id of the listener'}, 'callback': {'type': 'string', 'description': 'The callback being registered.'}, 'query': {'type': 'string', 'description': 'additional data to be passed'}}}, 'EventSubscriptionInput': {'type': 'object', 'description': 'Sets the communication endpoint address the service instance must use to deliver notification information', 'required': ['callback'], 'properties': {'callback': {'type': 'string', 'description': 'The callback being registered.'}, 'query': {'type': 'string', 'description': 'additional data to be passed'}}}, 'CustomerCreateEvent': {'type': 'object', 'description': 'The notification data structure', 'properties': {'id': {'type': 'string', 'description': 'Identifier of the resource involved in the event'}, 'href': {'type': 'string', 'description': 'Reference of the resource involved in the event'}, 'eventId': {'type': 'string', 'description': 'The identifier of the notification.'}, 'eventTime': {'type': 'string', 'format': 'date-time', 'description': 'Time of the event occurrence.'}, 'eventType': {'type': 'string', 'description': 'The type of the notification.'}, 'correlationId': {'type': 'string', 'description': 'The correlation id for this event.'}, 'domain': {'type': 'string', 'description': 'The domain of the event.'}, 'title': {'type': 'string', 'description': 'The title of the event.'}, 'description': {'type': 'string', 'description': 'An explanatory of the event.'}, 'priority': {'type': 'string', 'description': 'A priority.'}, 'timeOcurred': {'type': 'string', 'format': 'date-time', 'description': 'The time the event occured.'}, 'event': {'description': 'The event payload linked to the involved resource object', '$ref': '#/definitions/CustomerCreateEventPayload'}}}, 'CustomerCreateEventPayload': {'type': 'object', 'description': 'The event data structure', 'properties': {'customer': {'description': 'The involved resource data for the event', '$ref': '#/definitions/Customer'}}}, 'CustomerAttributeValueChangeEvent': {'type': 'object', 'description': 'The notification data structure', 'properties': {'eventId': {'type': 'string', 'description': 'The identifier of the notification.'}, 'eventTime': {'type': 'string', 'format': 'date-time', 'description': 'Time of the event occurrence.'}, 'eventType': {'type': 'string', 'description': 'The type of the notification.'}, 'correlationId': {'type': 'string', 'description': 'The correlation id for this event.'}, 'domain': {'type': 'string', 'description': 'The domain of the event.'}, 'title': {'type': 'string', 'description': 'The title of the event.'}, 'description': {'type': 'string', 'description': 'An explanatory of the event.'}, 'priority': {'type': 'string', 'description': 'A priority.'}, 'timeOcurred': {'type': 'string', 'format': 'date-time', 'description': 'The time the event occured.'}, 'fieldPath': {'type': 'string', 'description': 'The path identifying the object field concerned by this notification.'}, 'event': {'description': 'The event payload linked to the involved resource object', '$ref': '#/definitions/CustomerAttributeValueChangeEventPayload'}}}, 'CustomerAttributeValueChangeEventPayload': {'type': 'object', 'description': 'The event data structure', 'properties': {'customer': {'description': 'The involved resource data for the event', '$ref': '#/definitions/Customer'}}}, 'CustomerStateChangeEvent': {'type': 'object', 'description': 'The notification data structure', 'properties': {'id': {'type': 'string', 'description': 'Identifier of the resource involved in the event'}, 'href': {'type': 'string', 'description': 'Reference of the resource involved in the event'}, 'eventId': {'type': 'string', 'description': 'The identifier of the notification.'}, 'eventTime': {'type': 'string', 'format': 'date-time', 'description': 'Time of the event occurrence.'}, 'eventType': {'type': 'string', 'description': 'The type of the notification.'}, 'correlationId': {'type': 'string', 'description': 'The correlation id for this event.'}, 'domain': {'type': 'string', 'description': 'The domain of the event.'}, 'title': {'type': 'string', 'description': 'The title of the event.'}, 'description': {'type': 'string', 'description': 'An explanatory of the event.'}, 'priority': {'type': 'string', 'description': 'A priority.'}, 'timeOcurred': {'type': 'string', 'format': 'date-time', 'description': 'The time the event occured.'}, 'event': {'description': 'The event payload linked to the involved resource object', '$ref': '#/definitions/CustomerStateChangeEventPayload'}}}, 'CustomerStateChangeEventPayload': {'type': 'object', 'description': 'The event data structure', 'properties': {'customer': {'description': 'The involved resource data for the event', '$ref': '#/definitions/Customer'}}}, 'CustomerDeleteEvent': {'type': 'object', 'description': 'The notification data structure', 'properties': {'id': {'type': 'string', 'description': 'Identifier of the resource involved in the event'}, 'href': {'type': 'string', 'description': 'Reference of the resource involved in the event'}, 'eventId': {'type': 'string', 'description': 'The identifier of the notification.'}, 'eventTime': {'type': 'string', 'format': 'date-time', 'description': 'Time of the event occurrence.'}, 'eventType': {'type': 'string', 'description': 'The type of the notification.'}, 'correlationId': {'type': 'string', 'description': 'The correlation id for this event.'}, 'domain': {'type': 'string', 'description': 'The domain of the event.'}, 'title': {'type': 'string', 'description': 'The title of the event.'}, 'description': {'type': 'string', 'description': 'An explanatory of the event.'}, 'priority': {'type': 'string', 'description': 'A priority.'}, 'timeOcurred': {'type': 'string', 'format': 'date-time', 'description': 'The time the event occured.'}, 'event': {'description': 'The event payload linked to the involved resource object', '$ref': '#/definitions/CustomerDeleteEventPayload'}}}, 'CustomerDeleteEventPayload': {'type': 'object', 'description': 'The event data structure', 'properties': {'customer': {'description': 'The involved resource data for the event', '$ref': '#/definitions/Customer'}}}, 'Error': {'description': 'Used when an API throws an Error, typically with a HTTP error response-code (3xx, 4xx, 5xx)', 'type': 'object', 'required': ['code', 'reason'], 'properties': {'code': {'type': 'string', 'description': 'Application relevant detail, defined in the API or a common list.'}, 'reason': {'type': 'string', 'description': 'Explanation of the reason for the error which can be shown to a client user.'}, 'message': {'type': 'string', 'description': 'More details and corrective actions related to the error which can be shown to a client user.'}, 'status': {'type': 'string', 'description': 'HTTP Error code extension'}, 'referenceError': {'type': 'string', 'format': 'uri', 'description': 'URI of documentation describing the error.'}, '@baseType': {'type': 'string', 'description': 'When sub-classing, this defines the super-class.'}, '@schemaLocation': {'type': 'string', 'format': 'uri', 'description': 'A URI to a JSON-Schema file that defines additional attributes and relationships'}, '@type': {'type': 'string', 'description': 'When sub-classing, this defines the sub-class entity name.'}}}}, 'parameters': {}}

validators = {
    ('customer', 'GET'): {'args': {'required': [], 'properties': {'fields': {'description': 'Comma-separated properties to be provided in response', 'required': False, 'type': 'string'}, 'offset': {'description': 'Requested index for start of resources to be provided in response', 'required': False, 'type': 'integer'}, 'limit': {'description': 'Requested number of resources to be provided in response', 'required': False, 'type': 'integer'}}}},
    ('customer', 'POST'): {'json': {'$ref': '#/definitions/Customer_Create'}},
    ('customer_id', 'GET'): {'args': {'required': [], 'properties': {'fields': {'description': 'Comma-separated properties to provide in response', 'required': False, 'type': 'string'}}}},
    ('customer_id', 'PATCH'): {'json': {'$ref': '#/definitions/Customer_Update'}},
    ('hub', 'POST'): {'json': {'$ref': '#/definitions/EventSubscriptionInput'}},
    ('listener_customerCreateEvent', 'POST'): {'json': {'$ref': '#/definitions/CustomerCreateEvent'}},
    ('listener_customerAttributeValueChangeEvent', 'POST'): {'json': {'$ref': '#/definitions/CustomerAttributeValueChangeEvent'}},
    ('listener_customerStateChangeEvent', 'POST'): {'json': {'$ref': '#/definitions/CustomerStateChangeEvent'}},
    ('listener_customerDeleteEvent', 'POST'): {'json': {'$ref': '#/definitions/CustomerDeleteEvent'}},
}

filters = {
    ('customer', 'GET'): {200: {'headers': {'X-Result-Count': {'description': 'Actual number of items returned in the response body', 'type': 'integer'}, 'X-Total-Count': {'description': 'Total number of items matching criteria', 'type': 'integer'}}, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/Customer'}}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('customer', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Customer'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('customer_id', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Customer'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('customer_id', 'PATCH'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Customer'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('customer_id', 'DELETE'): {204: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('hub', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/EventSubscription'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('hub_id', 'DELETE'): {204: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('listener_customerCreateEvent', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/EventSubscription'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('listener_customerAttributeValueChangeEvent', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/EventSubscription'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('listener_customerStateChangeEvent', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/EventSubscription'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
    ('listener_customerDeleteEvent', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/EventSubscription'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 401: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 405: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}, 500: {'headers': None, 'schema': {'$ref': '#/definitions/Error'}}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
