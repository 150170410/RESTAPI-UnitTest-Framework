import base64
import hashlib
import os.path
import random
import string
import time
import uuid
from datetime import datetime, timedelta

import pytz


class DataGenerator:
    max_int = 2147483647
    min_int = -2147483647
    max_int16 = 32767
    max_int8 = 127

    default_date_format = '%Y-%m-%d'
    default_date_time_format = '%Y-%m-%d %H:%M:%S'
    time_zone_moscow = pytz.timezone('Europe/Moscow')

    @staticmethod
    def generate_random_string(length=5, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def generate_random_integer(length=7, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def generate_random_bool():
        return random.choice([True, False])

    def generate_bad_str(self):
        bad_values = [
            ' ',
            random.randint(self.min_int, self.max_int),
        ]
        return random.choice(bad_values)

    def generate_bad_int(self):
        bad_values = [
            ' ',
            self.generate_random_string(random.randint(0, 100)),
        ]
        return random.choice(bad_values)

    @staticmethod
    def generate_negative_or_zero():
        return str(random.choice([-1, 0]))

    def generate_empty_or_random_string(self):
        values = [
            ' ',
            self.generate_random_string(),
        ]
        return random.choice(values)

    def generate_number_or_zero(self):
        values = [
            '0',
            random.randint(self.min_int, self.max_int),
        ]
        return random.choice(values)

    def generate_bad_beta_int(self):
        return str(random.randrange(2, self.max_int))

    @staticmethod
    def merge_params(params_1, params_2):
        return {**params_1, **params_2}
