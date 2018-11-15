from testlib.data_generator import *


class reqResDataGenerator(DataGenerator):
    @staticmethod
    def provider_users():
        return lambda: (
            ('1',),
            ('2',),
            ('3',),

        )
