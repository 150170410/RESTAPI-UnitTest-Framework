from unittest_data_provider import data_provider

from testlib.reqResUsers.reqResMainTest import *
from testlib.reqResUsers.reqRes_data_generators import reqResDataGenerator


class reqResUsersTests(reqResMainTestCase):
    def test_get_users(self):
        response = self.send_api_request(self.request_endpoint,
                                         auth=None)
        self.assert_code_ok(response)
        self.assertEqual(response['response']['per_page'], 3)

    @data_provider(reqResDataGenerator.provider_users())
    def test_get_single_user(self, param):
        response = self.send_api_request(f'{self.request_endpoint}/{param}',
                                         auth=None)
        self.assert_code_ok(response)

    def test_get_invalid_user(self):
        response = self.send_api_request(f'{self.request_endpoint}/{51}',
                                         auth=None)
        self.assert_not_found_request_code(response)
