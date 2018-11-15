from testlib.main_test_case import *
from testlib.reqResUsers.reqRes_data_generators import *


class reqResMainTestCase(MainTestCase):
    request_endpoint = 'users'


    def setUp(self):
        super().setUp()

    @classmethod
    def preparations_before_tests(cls):
        super().preparations_before_tests()

    @classmethod
    def read_tests_config(cls):
        super().read_tests_config()
        cls.cfg_host = cls.config['typiCode']['host']

    def get_request_url(self, request):
        return f'/{request}'

    def send_api_request(self, request, params=None, auth=None, decode_resp=True, request_type='get', data=None,
                         headers=None, need_headers=False):
        request = self.get_request_url(request)
        headers = self.get_headers(auth, headers)
        return self.make_request(request=request,
                                 params=params,
                                 headers=headers,
                                 decode_resp=decode_resp,
                                 request_type=request_type,
                                 data=data,
                                 need_headers=need_headers)

    def get_headers(self, auth, headers=None):
        if not headers:
            headers = {}
        if auth:
            header_auth = auth
        else:
            header_auth = {
                False: {'X-Authorization': f'Basic {auth}'},
                None: {},
            }[auth]
        return {**headers, **header_auth}
