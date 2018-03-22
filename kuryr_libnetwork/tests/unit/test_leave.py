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

import ddt
from oslo_serialization import jsonutils
from werkzeug import exceptions as w_exceptions

from kuryr.lib import utils as lib_utils
from kuryr_libnetwork.tests.unit import base


@ddt.ddt
class TestKuryrLeaveFailures(base.TestKuryrFailures):
    """Unit tests for the failures for leaving the namespace."""
    def _invoke_leave_request(self, docker_network_id,
                              docker_endpoint_id):
        data = {
            'NetworkID': docker_network_id,
            'EndpointID': docker_endpoint_id,
        }
        response = self.app.post('/NetworkDriver.Leave',
                                 content_type='application/json',
                                 data=jsonutils.dumps(data))

        return response

    def test_leave_bad_request(self):
        fake_docker_network_id = lib_utils.get_hash()
        invalid_docker_endpoint_id = 'id-should-be-hexdigits'

        response = self._invoke_leave_request(
            fake_docker_network_id, invalid_docker_endpoint_id)

        self.assertEqual(w_exceptions.BadRequest.code, response.status_code)
        decoded_json = jsonutils.loads(response.data)
        self.assertIn('Err', decoded_json)
        # TODO(tfukushima): Add the better error message validation.
        self.assertIn(invalid_docker_endpoint_id, decoded_json['Err'])
        self.assertIn('EndpointID', decoded_json['Err'])
