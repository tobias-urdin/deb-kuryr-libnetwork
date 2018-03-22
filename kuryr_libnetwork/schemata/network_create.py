# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from kuryr_libnetwork.schemata import commons

NETWORK_CREATE_SCHEMA = {
    u'links': [{
        u'method': u'POST',
        u'href': u'/NetworkDriver.CreateNetwork',
        u'description': u'Create a Network',
        u'rel': u'self',
        u'title': u'Create'
    }],
    u'title': u'Create network',
    u'required': [u'NetworkID', u'IPv4Data', u'IPv6Data'],
    u'definitions': {u'commons': {}},
    u'$schema': u'http://json-schema.org/draft-04/hyper-schema',
    u'type': u'object',
    u'properties': {
        u'NetworkID': {
            u'description': u'ID of a Network to be created',
            u'$ref': u'#/definitions/commons/definitions/id'
        },
        u'IPv4Data': {
            u'description': u'IPv4 data for the network',
            u'type': u'array',
            u'items': {
                u'$ref': u'#/definitions/commons/definitions/ipv4datum'
            }
        },
        u'IPv6Data': {
            u'description': u'IPv6 data for the network',
            u'type': u'array',
            u'items': {
                u'$ref': u'#/definitions/commons/definitions/ipv6datum'
            }
        },
        u'Options': {
            u'type': [u'object', u'null'],
            u'description': u'Options',
            u'example': {}
        }
    }
}

NETWORK_CREATE_SCHEMA[u'definitions'][u'commons'] = commons.COMMONS
