import unittest

from avasdk.exceptions import ValidationError
from avasdk.validate_plugin import validate_plugin

from . import ConfigSetup

class TestGlobalValidatorConfing(ConfigSetup, unittest.TestCase):

    def test_corect_name(self):
        # should not raise exception
        validate_plugin(self.good_config)

    def test_wrong_name(self):
        # should not raise exception
        validate_plugin(self.wrong_name_config)
