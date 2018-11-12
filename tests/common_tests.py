import unittest
from zb_common import Util
from parameterized import parameterized

util = Util('test.cfg', "zb-common")

class ZBCommonTests(unittest.TestCase):

    # get_E164_US_phone_number
    @parameterized.expand([
        ("(123) 456-7890"),
        ("+11234567890"),
        ("123-456-7890")
    ])
    def test_get_E164_US_phone_number(self, us_phone_number):
        ret_val = util.get_E164_US_phone_number(us_phone_number)
        print("input ph number:{}, ret_val: {}".format(us_phone_number, ret_val))
        assert(ret_val == "+11234567890")
